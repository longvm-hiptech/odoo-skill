# -*- coding: utf-8 -*-
from __future__ import annotations

import datetime
from typing import Any, Optional
from odoo import api, fields, models, Command, _
from odoo.exceptions import UserError

class QmsSopTrainingPlan(models.Model):
    _name = 'qms.sop.training.plan'
    _description = 'QMS SOP Training Plan'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'deadline asc, name desc'
    _check_company_auto = True

    name: str = fields.Char(
        string='Plan Title',
        required=True,
        tracking=True,
    )
    sop_id: int = fields.Many2one(
        comodel_name='qms.sop',
        string='Target SOP',
        required=True,
        tracking=True,
        check_company=True,
    )
    coordinator_id: int = fields.Many2one(
        comodel_name='res.users',
        string='Training Coordinator',
        default=lambda self: self.env.user,
        required=True,
        tracking=True,
        check_company=True,
    )
    deadline: datetime.date = fields.Date(
        string='Training Deadline',
        default=lambda self: fields.Date.context_today(self) + datetime.timedelta(days=30),
        required=True,
        tracking=True,
    )
    employee_ids: list = fields.Many2many(
        comodel_name='res.users',
        relation='qms_training_users_rel',
        column1='plan_id',
        column2='user_id',
        string='Employees to Train',
        required=True,
    )
    record_ids: list = fields.One2many(
        comodel_name='qms.sop.training.record',
        inverse_name='plan_id',
        string='Training Records',
    )
    state: str = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('active', 'Active (In Progress)'),
            ('completed', 'Completed'),
        ],
        string='Status',
        default='draft',
        required=True,
        tracking=True,
        copy=False,
    )
    company_id: int = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        default=lambda self: self.env.company,
        required=True,
        index=True,
    )
    active: bool = fields.Boolean(
        default=True,
    )

    @api.model_create_multi
    def create(self, vals_list: list[dict[str, Any]]) -> QmsSopTrainingPlan:
        """Generate sequence on creation."""
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New') or not vals.get('name'):
                vals['name'] = self.env['ir.sequence'].next_by_code('qms.sop.training.plan') or _('New')
        return super().create(vals_list)

    def action_activate(self) -> None:
        """Activate the training plan and generate records for employees."""
        for record in self:
            if record.state != 'draft':
                continue
            if not record.employee_ids:
                raise UserError(_("Please select at least one employee to train."))
            
            # Create training records using Command.create (Odoo 19 style)
            records_vals = []
            for emp in record.employee_ids:
                records_vals.append(Command.create({
                    'user_id': emp.id,
                    'company_id': record.company_id.id,
                    'state': 'pending',
                }))
            
            record.write({
                'state': 'active',
                'record_ids': records_vals,
            })
            
            # Move SOP to Training Phase if linked
            if record.sop_id.state == 'approve':
                record.sop_id.action_start_training()

    def action_check_completion(self) -> None:
        """Check if all employees passed their training to complete the plan."""
        for record in self:
            if record.state != 'active':
                continue
            # If all records are passed, mark plan as completed
            if record.record_ids and all(rec.state == 'passed' for rec in record.record_ids):
                record.write({'state': 'completed'})
                # Notify QA that training is completed and SOP can be activated
                record.sop_id.message_post(body=_(
                    "Training Plan '%s' is completed. SOP can now be activated.",
                    record.name
                ))


class QmsSopTrainingRecord(models.Model):
    _name = 'qms.sop.training.record'
    _description = 'QMS SOP Training Record'
    _order = 'user_id'
    _check_company_auto = True

    plan_id: int = fields.Many2one(
        comodel_name='qms.sop.training.plan',
        string='Training Plan',
        required=True,
        ondelete='cascade',
    )
    sop_id: int = fields.Many2one(
        comodel_name='qms.sop',
        string='SOP Document',
        related='plan_id.sop_id',
        store=True,
        index=True,
    )
    user_id: int = fields.Many2one(
        comodel_name='res.users',
        string='Employee',
        required=True,
        check_company=True,
    )
    date_completed: datetime.date = fields.Date(
        string='Completion Date',
        readonly=True,
    )
    state: str = fields.Selection(
        selection=[
            ('pending', 'Pending (Chưa đào tạo)'),
            ('passed', 'Passed (Đã đạt)'),
            ('failed', 'Failed (Không đạt)'),
        ],
        string='Evaluation',
        default='pending',
        required=True,
    )
    company_id: int = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        default=lambda self: self.env.company,
        required=True,
        index=True,
    )

    def action_pass(self) -> None:
        """Mark record as passed and check if plan can be completed."""
        self.write({
            'state': 'passed',
            'date_completed': fields.Date.context_today(self),
        })
        for record in self:
            record.plan_id.action_check_completion()

    def action_fail(self) -> None:
        """Mark record as failed."""
        self.write({
            'state': 'failed',
            'date_completed': False,
        })
