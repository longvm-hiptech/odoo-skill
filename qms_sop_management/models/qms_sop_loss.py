# -*- coding: utf-8 -*-
from __future__ import annotations

import datetime
from typing import Any, Optional
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class QmsSopLoss(models.Model):
    _name = 'qms.sop.loss'
    _description = 'QMS SOP Document Loss Report'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'loss_date desc, name desc'
    _check_company_auto = True

    name: str = fields.Char(
        string='Loss Report ID',
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _('New'),
        tracking=True,
    )
    sop_id: int = fields.Many2one(
        comodel_name='qms.sop',
        string='SOP Document',
        required=True,
        tracking=True,
        check_company=True,
    )
    sop_code: str = fields.Char(
        string='SOP Code',
        related='sop_id.code',
        readonly=True,
    )
    reporter_id: int = fields.Many2one(
        comodel_name='res.users',
        string='Reporter',
        default=lambda self: self.env.user,
        required=True,
        tracking=True,
        check_company=True,
    )
    loss_date: datetime.date = fields.Date(
        string='Loss Date',
        default=fields.Date.context_today,
        required=True,
        tracking=True,
    )
    description: str = fields.Text(
        string='Description of Loss Event',
        required=True,
        tracking=True,
    )
    state: str = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('reported', 'Reported'),
            ('resolved', 'Resolved'),
        ],
        string='Status',
        default='draft',
        required=True,
        tracking=True,
        copy=False,
    )
    resolution_notes: str = fields.Text(
        string='QA Resolution Notes',
        tracking=True,
    )
    company_id: int = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        default=lambda self: self.env.company,
        required=True,
        index=True,
    )

    @api.model_create_multi
    def create(self, vals_list: list[dict[str, Any]]) -> QmsSopLoss:
        """Generate sequence on creation."""
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('qms.sop.loss') or _('New')
        return super().create(vals_list)

    def action_report(self) -> None:
        """Report loss to QA."""
        self.write({'state': 'reported'})

    def action_resolve(self) -> None:
        """Resolve the loss report by QA."""
        for record in self:
            if not record.resolution_notes:
                raise UserError(_("Please write resolution notes before resolving the loss report."))
            record.write({'state': 'resolved'})
