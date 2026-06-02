# -*- coding: utf-8 -*-
from __future__ import annotations

import datetime
from typing import Any, Optional
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class QmsSopSpell(models.Model):
    _name = 'qms.sop.spell'
    _description = 'QMS SOP Spelling Correction Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'request_date desc, name desc'
    _check_company_auto = True

    name: str = fields.Char(
        string='Correction ID',
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _('New'),
        tracking=True,
    )
    sop_id: int = fields.Many2one(
        comodel_name='qms.sop',
        string='Target SOP',
        required=True,
        tracking=True,
        check_company=True,
    )
    requester_id: int = fields.Many2one(
        comodel_name='res.users',
        string='Requester',
        default=lambda self: self.env.user,
        required=True,
        tracking=True,
        check_company=True,
    )
    request_date: datetime.date = fields.Date(
        string='Request Date',
        default=fields.Date.context_today,
        required=True,
        tracking=True,
    )
    correction_details: str = fields.Text(
        string='Spelling Correction Details',
        required=True,
        tracking=True,
        help='Describe clearly what is wrong, what the correct spelling is, and where it is located.',
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
    approver_id: int = fields.Many2one(
        comodel_name='res.users',
        string='Approver (QA)',
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

    @api.model_create_multi
    def create(self, vals_list: list[dict[str, Any]]) -> QmsSopSpell:
        """Generate sequence on creation."""
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('qms.sop.spell') or _('New')
        return super().create(vals_list)

    def action_submit(self) -> None:
        """Submit the spelling request."""
        self.write({'state': 'submitted'})

    def action_approve(self) -> None:
        """Approve the spelling request."""
        self.write({
            'state': 'approved',
            'approver_id': self.env.user.id,
        })
        # Note: In a real implementation, QA would apply this correction to a draft revision.

    def action_reject(self) -> None:
        """Reject the spelling request."""
        self.write({'state': 'rejected'})
