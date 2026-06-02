# -*- coding: utf-8 -*-
from __future__ import annotations

import datetime
from typing import Any, Optional
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class QmsSopDistribution(models.Model):
    _name = 'qms.sop.distribution'
    _description = 'QMS SOP Copy Distribution & Recall'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date_printed desc, name desc'
    _check_company_auto = True

    name: str = fields.Char(
        string='Distribution ID',
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
    print_type: str = fields.Selection(
        selection=[
            ('controlled', 'Controlled Copy (Bản kiểm soát)'),
            ('reference', 'Reference Copy (Bản tham khảo)'),
            ('uncontrolled', 'Uncontrolled Copy (Bản không kiểm soát)'),
        ],
        string='Print Copy Type',
        required=True,
        default='controlled',
        tracking=True,
    )
    user_id: int = fields.Many2one(
        comodel_name='res.users',
        string='Printed/Issued By',
        default=lambda self: self.env.user,
        required=True,
        tracking=True,
        check_company=True,
    )
    department_id: int = fields.Many2one(
        comodel_name='hr.department',
        string='Recipient Department',
        tracking=True,
    )
    usage_location: str = fields.Char(
        string='Usage Location/Position',
        required=True,
        tracking=True,
    )
    print_qty: int = fields.Integer(
        string='Print Quantity',
        required=True,
        default=1,
        tracking=True,
    )
    date_printed: datetime.date = fields.Date(
        string='Print Date',
        default=fields.Date.context_today,
        required=True,
        tracking=True,
    )
    state: str = fields.Selection(
        selection=[
            ('issued', 'Issued'),
            ('recalled', 'Recalled'),
        ],
        string='Status',
        default='issued',
        required=True,
        tracking=True,
        copy=False,
    )
    date_recalled: datetime.date = fields.Date(
        string='Recall Date',
        readonly=True,
        copy=False,
    )
    recaller_id: int = fields.Many2one(
        comodel_name='res.users',
        string='Recalled By',
        readonly=True,
        copy=False,
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

    @api.constrains('print_qty')
    def _check_print_qty(self) -> None:
        """Validate print quantity is positive."""
        for record in self:
            if record.print_qty <= 0:
                raise ValidationError(_("Print quantity must be greater than zero."))

    @api.model_create_multi
    def create(self, vals_list: list[dict[str, Any]]) -> QmsSopDistribution:
        """Generate sequence on creation."""
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('qms.sop.distribution') or _('New')
        return super().create(vals_list)

    def action_recall(self) -> None:
        """Recall the distributed copies."""
        self.write({
            'state': 'recalled',
            'date_recalled': fields.Date.context_today(self),
            'recaller_id': self.env.user.id,
        })

    def action_print_copy(self) -> dict[str, Any]:
        """Print the SOP document with watermark context from distribution record."""
        self.ensure_one()
        type_labels = {
            'controlled': _('CONTROLLED COPY'),
            'reference': _('REFERENCE COPY'),
            'uncontrolled': _('UNCONTROLLED COPY'),
        }
        
        report_action = self.env.ref('qms_sop_management.action_report_qms_sop').report_action(self.sop_id.id)
        
        report_context = {
            'print_type_label': type_labels.get(self.print_type, _('UNCONTROLLED COPY')),
            'print_recipient': self.department_id.name or _('N/A'),
            'print_issuer': self.user_id.name,
            'print_date': fields.Date.to_string(self.date_printed),
            'print_location': self.usage_location,
        }
        
        report_action.setdefault('context', {})
        report_action['context'].update(report_context)
        return report_action
