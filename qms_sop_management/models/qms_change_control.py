# -*- coding: utf-8 -*-
from __future__ import annotations

import datetime
from typing import Any, Optional
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class QmsChangeControl(models.Model):
    _name = 'qms.change.control'
    _description = 'QMS Change Control'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name desc'
    _check_company_auto = True

    name: str = fields.Char(
        string='Change Request ID',
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _('New'),
        tracking=True,
    )
    description: str = fields.Text(
        string='Description of Change',
        required=True,
        tracking=True,
    )
    reason: str = fields.Text(
        string='Reason for Change',
        required=True,
        tracking=True,
    )
    request_date: datetime.date = fields.Date(
        string='Request Date',
        default=fields.Date.context_today,
        required=True,
        tracking=True,
    )
    requester_id: int = fields.Many2one(
        comodel_name='res.users',
        string='Requester',
        default=lambda self: self.env.user,
        required=True,
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
    state: str = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('submitted', 'Submitted'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
        ],
        string='Status',
        default='draft',
        required=True,
        tracking=True,
        copy=False,
    )
    sop_ids: list = fields.One2many(
        comodel_name='qms.sop',
        inverse_name='change_control_id',
        string='Affected SOPs',
    )

    @api.model_create_multi
    def create(self, vals_list: list[dict[str, Any]]) -> QmsChangeControl:
        """Generate sequence on creation."""
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('qms.change.control') or _('New')
        return super().create(vals_list)

    def write(self, vals: dict[str, Any]) -> bool:
        """Write with restrictions based on state."""
        if 'state' in vals:
            if vals['state'] == 'approved' and any(rec.state != 'submitted' for rec in self):
                raise UserError(_("Only submitted requests can be approved."))
        return super().write(vals)

    def unlink(self) -> bool:
        """Prevent deletion of non-draft change controls."""
        if any(rec.state != 'draft' for rec in self):
            raise UserError(_("Cannot delete change controls that are not in Draft state."))
        return super().unlink()

    def action_submit(self) -> None:
        """Submit the change request."""
        self.write({'state': 'submitted'})

    def action_approve(self) -> None:
        """Approve the change request."""
        self.write({'state': 'approved'})

    def action_reject(self) -> None:
        """Reject the change request."""
        self.write({'state': 'rejected'})
