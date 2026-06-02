# -*- coding: utf-8 -*-
from __future__ import annotations

import datetime
from typing import Any, Optional
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class QmsSop(models.Model):
    _name = 'qms.sop'
    _description = 'QMS Standard Operating Procedure'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'code desc, edition_num desc'
    _check_company_auto = True

    name: str = fields.Char(
        string='SOP Title',
        required=True,
        tracking=True,
    )
    code: str = fields.Char(
        string='SOP Code',
        copy=False,
        readonly=True,
        tracking=True,
        index='btree',
    )
    building_code: str = fields.Selection(
        selection=[
            ('B1', 'Building 1 (B1)'),
            ('B2', 'Building 2 (B2)'),
            ('B3', 'Building 3 (B3)'),
        ],
        string='Building Code',
        required=True,
        default='B1',
        tracking=True,
    )
    dept_code: str = fields.Selection(
        selection=[
            ('QA', 'Quality Assurance (QA)'),
            ('QC', 'Quality Control (QC)'),
            ('PR', 'Production (PR)'),
            ('HR', 'Human Resources (HR)'),
            ('LOG', 'Logistics (LOG)'),
            ('MA', 'Maintenance (MA)'),
        ],
        string='Department Code',
        required=True,
        default='QA',
        tracking=True,
    )
    seq_num: int = fields.Integer(
        string='Sequence Number',
        readonly=True,
        copy=False,
    )
    edition_num: int = fields.Integer(
        string='Edition/Version (TT)',
        default=1,
        readonly=True,
        copy=False,
    )
    file_binary: bytes = fields.Binary(
        string='SOP File (Word/PDF)',
        attachment=True,
    )
    file_name: str = fields.Char(
        string='File Name',
    )
    owner_id: int = fields.Many2one(
        comodel_name='res.users',
        string='Owner (Dept Head)',
        required=True,
        default=lambda self: self.env.user,
        tracking=True,
        check_company=True,
    )
    checker_ids: list = fields.Many2many(
        comodel_name='res.users',
        relation='qms_sop_checker_rel',
        column1='sop_id',
        column2='user_id',
        string='Checkers/Reviewers',
        tracking=True,
        check_company=True,
    )
    approver_id: int = fields.Many2one(
        comodel_name='res.users',
        string='Approver (QA Manager)',
        readonly=True,
        tracking=True,
        check_company=True,
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
    state: str = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('review', 'Under Review'),
            ('approve', 'Approved'),
            ('training', 'Training Phase'),
            ('effective', 'Effective'),
            ('obsolete', 'Obsoleted'),
        ],
        string='Status',
        default='draft',
        required=True,
        tracking=True,
        copy=False,
    )
    date_approved: datetime.date = fields.Date(
        string='Approval Date',
        readonly=True,
        copy=False,
    )
    date_effective: datetime.date = fields.Date(
        string='Effective Date',
        readonly=True,
        copy=False,
    )
    date_review_deadline: datetime.date = fields.Date(
        string='Review Deadline',
        readonly=True,
        copy=False,
    )
    review_without_change_count: int = fields.Integer(
        string='Review Without Change Count',
        default=0,
        readonly=True,
        copy=False,
    )
    change_control_id: int = fields.Many2one(
        comodel_name='qms.change.control',
        string='Change Control Ref',
        tracking=True,
        check_company=True,
    )
    parent_sop_id: int = fields.Many2one(
        comodel_name='qms.sop',
        string='Previous SOP Version',
        readonly=True,
        copy=False,
    )
    child_sop_ids: list = fields.One2many(
        comodel_name='qms.sop',
        inverse_name='parent_sop_id',
        string='Newer SOP Versions',
    )
    form_ids: list = fields.One2many(
        comodel_name='qms.sop.form',
        inverse_name='sop_id',
        string='Associated Forms',
    )
    logbook_ids: list = fields.One2many(
        comodel_name='qms.sop.logbook',
        inverse_name='sop_id',
        string='Associated Logbooks',
    )

    @api.constrains('file_binary')
    def _check_file(self) -> None:
        """Ensure file is attached when leaving draft state."""
        for record in self:
            if record.state != 'draft' and not record.file_binary:
                raise ValidationError(_("Please upload the SOP document file before proceeding."))

    @api.model_create_multi
    def create(self, vals_list: list[dict[str, Any]]) -> QmsSop:
        """Create multi-records, checking parent links."""
        for vals in vals_list:
            if vals.get('parent_sop_id'):
                parent = self.browse(vals['parent_sop_id'])
                # If creating from a parent, copy sequence and department/building metadata
                vals['seq_num'] = parent.seq_num
                vals['building_code'] = parent.building_code
                vals['dept_code'] = parent.dept_code
                vals['edition_num'] = parent.edition_num + 1
            else:
                vals['edition_num'] = 1
        return super().create(vals_list)

    def write(self, vals: dict[str, Any]) -> bool:
        """Validate state updates and auto-generate code."""
        if 'building_code' in vals or 'dept_code' in vals:
            for record in self:
                if record.state != 'draft':
                    raise UserError(_("Cannot change building or department codes for a non-draft SOP."))
        return super().write(vals)

    def unlink(self) -> bool:
        """Allow deleting only draft SOPs."""
        if any(rec.state != 'draft' for rec in self):
            raise UserError(_("Only draft SOPs can be deleted."))
        return super().unlink()

    # === LIFECYCLE ACTIONS === #

    def action_submit_review(self) -> None:
        """Submit SOP for internal checking/review by checkers."""
        for record in self:
            if not record.checker_ids:
                raise UserError(_("Please assign at least one Checker/Reviewer before submitting for review."))
            record.write({'state': 'review'})

    def action_approve(self) -> None:
        """QA Manager approves the SOP. Sets approval date and generated code."""
        for record in self:
            # Assign sequence number if it does not exist yet (i.e. first edition)
            seq = record.seq_num
            if not seq:
                # Find maximum sequence number for the same building and department
                domain = [
                    ('building_code', '=', record.building_code),
                    ('dept_code', '=', record.dept_code),
                    ('seq_num', '>', 0),
                ]
                existing_sops = self.search(domain, order='seq_num desc', limit=1)
                seq = (existing_sops.seq_num + 1) if existing_sops else 1

            code_str = f"{record.building_code}.{record.dept_code}.{seq:04d}-{record.edition_num:02d}"
            
            record.write({
                'state': 'approve',
                'approver_id': self.env.user.id,
                'seq_num': seq,
                'code': code_str,
                'date_approved': fields.Date.context_today(self),
            })

    def action_start_training(self) -> None:
        """Move the SOP to the training phase."""
        self.write({'state': 'training'})

    def action_set_effective(self) -> None:
        """Activate the SOP. Obsoletes previous parent version."""
        today = fields.Date.context_today(self)
        for record in self:
            # Check training records (this will be used by the training module)
            # Set review deadline (e.g. 2 years = 730 days from effective date)
            deadline = today + datetime.timedelta(days=730)
            record.write({
                'state': 'effective',
                'date_effective': today,
                'date_review_deadline': deadline,
            })
            
            # Obsolete parent SOP if exists
            if record.parent_sop_id:
                record.parent_sop_id.action_obsolete()

    def action_renew_without_change(self) -> None:
        """Renew SOP without changes for another cycle (2 years), up to 2 times."""
        for record in self:
            if record.state != 'effective':
                raise UserError(_("Only effective SOPs can be renewed."))
            if record.review_without_change_count >= 2:
                raise UserError(_(
                    "SOP này đã được gia hạn không thay đổi 2 lần. "
                    "Bắt buộc phải tạo Phiếu kiểm soát thay đổi (Change Control) để cập nhật nội dung SOP."
                ))
            today = fields.Date.context_today(self)
            new_deadline = today + datetime.timedelta(days=730)
            record.write({
                'review_without_change_count': record.review_without_change_count + 1,
                'date_review_deadline': new_deadline,
            })
            record.message_post(body=_(
                "SOP đã được gia hạn không sửa đổi (Gia hạn lần %d). Hạn review tiếp theo: %s",
                record.review_without_change_count,
                new_deadline
            ))

    def action_obsolete(self) -> None:
        """Set older SOP version as obsoleted."""
        self.write({'state': 'obsolete'})

    def action_reset_draft(self) -> None:
        """Reset SOP back to draft status for adjustments."""
        self.write({'state': 'draft'})

    def action_create_new_edition(self) -> dict[str, Any]:
        """Convenience action to create a new revision draft from current SOP."""
        self.ensure_one()
        if self.state != 'effective':
            raise UserError(_("You can only create a new revision from an Effective SOP."))
        
        # Check if there is already a draft revision in progress
        existing_draft = self.search([
            ('parent_sop_id', '=', self.id),
            ('state', 'in', ('draft', 'review', 'approve', 'training')),
        ], limit=1)
        if existing_draft:
            raise UserError(_("A draft revision for this SOP is already in progress: %s", existing_draft.name))

        # Create new record
        new_sop = self.create([{
            'name': self.name,
            'parent_sop_id': self.id,
            'change_control_id': self.change_control_id.id if self.change_control_id else False,
            'company_id': self.company_id.id,
        }])

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'qms.sop',
            'res_id': new_sop.id,
            'view_mode': 'form',
            'target': 'current',
        }

    def action_create_training_plan(self) -> dict[str, Any]:
        """Create or open the training plan for this SOP."""
        self.ensure_one()
        # Find existing plan
        plan = self.env['qms.sop.training.plan'].search([
            ('sop_id', '=', self.id),
            ('state', 'in', ('draft', 'active')),
        ], limit=1)

        if not plan:
            # Create a new draft plan prefilled with standard settings
            plan = self.env['qms.sop.training.plan'].create([{
                'name': _("Đào tạo SOP: %s", self.name),
                'sop_id': self.id,
                'company_id': self.company_id.id,
            }])

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'qms.sop.training.plan',
            'res_id': plan.id,
            'view_mode': 'form',
            'target': 'current',
        }

    @api.model
    def _cron_weekly_task_reminder(self) -> None:
        """Find pending SOP tasks and post a weekly reminder message on chatter."""
        sops = self.search([('state', 'in', ('draft', 'review', 'training'))])
        for record in sops:
            record.message_post(
                body=_("Weekly reminder: This SOP is still in '%s' state and requires action.", record.state),
                message_type='comment',
            )

    @api.model
    def _cron_check_expiring_sops(self) -> None:
        """Find SOPs expiring in 90 days, create a review activity for the owner."""
        today = fields.Date.context_today(self)
        target_date = today + datetime.timedelta(days=90)
        sops = self.search([
            ('state', '=', 'effective'),
            ('date_review_deadline', '<=', target_date),
            ('date_review_deadline', '>=', today),
        ])
        
        activity_type = self.env.ref('mail.mail_activity_data_todo', raise_if_not_found=False)
        for record in sops:
            # Check if review activity already exists to avoid duplicates
            existing = self.env['mail.activity'].search([
                ('res_model', '=', self._name),
                ('res_id', '=', record.id),
                ('summary', '=', _("SOP Review Required")),
            ])
            if not existing:
                self.env['mail.activity'].create({
                    'activity_type_id': activity_type.id if activity_type else False,
                    'res_model_id': self.env['ir.model']._get_id(self._name),
                    'res_id': record.id,
                    'summary': _("SOP Review Required"),
                    'note': _("SOP is expiring in 3 months on %s. Please review it.", record.date_review_deadline),
                    'user_id': record.owner_id.id,
                    'date_deadline': record.date_review_deadline,
                })
