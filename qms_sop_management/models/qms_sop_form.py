# -*- coding: utf-8 -*-
from __future__ import annotations

from typing import Any, Optional
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class QmsSopForm(models.Model):
    _name = 'qms.sop.form'
    _description = 'QMS SOP Associated Form'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'code desc'
    _check_company_auto = True

    name: str = fields.Char(
        string='Form Name',
        required=True,
        tracking=True,
    )
    code: str = fields.Char(
        string='Form Code',
        copy=False,
        readonly=True,
        tracking=True,
        index='btree',
    )
    sop_id: int = fields.Many2one(
        comodel_name='qms.sop',
        string='Associated SOP',
        required=True,
        ondelete='cascade',
        tracking=True,
        check_company=True,
    )
    form_type: str = fields.Selection(
        selection=[
            ('S', 'Paper Form (S)'),
            ('E', 'Electronic Form (E)'),
            ('A', 'Appendix (A)'),
        ],
        string='Form Type',
        required=True,
        default='S',
        tracking=True,
    )
    seq_num: int = fields.Integer(
        string='Form Sequence (AA)',
        readonly=True,
        copy=False,
    )
    edition_num: int = fields.Integer(
        string='Form Version (FF)',
        default=1,
        readonly=True,
        copy=False,
    )
    is_electronic: bool = fields.Boolean(
        string='Is Electronic Form?',
        compute='_compute_is_electronic',
        store=True,
    )
    file_binary: bytes = fields.Binary(
        string='Form Template File',
        attachment=True,
    )
    file_name: str = fields.Char(
        string='File Name',
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

    @api.depends('form_type')
    def _compute_is_electronic(self) -> None:
        """Compute whether the form is filled electronically."""
        for record in self:
            record.is_electronic = (record.form_type == 'E')

    @api.model_create_multi
    def create(self, vals_list: list[dict[str, Any]]) -> QmsSopForm:
        """Create multi-records and auto-generate Form Code."""
        for vals in vals_list:
            sop = self.env['qms.sop'].browse(vals['sop_id'])
            
            # Find max form sequence number (AA) for the same SOP and type
            domain = [
                ('sop_id', '=', vals['sop_id']),
                ('form_type', '=', vals['form_type']),
                ('seq_num', '>', 0),
            ]
            existing_forms = self.search(domain, order='seq_num desc', limit=1)
            seq = (existing_forms.seq_num + 1) if existing_forms else 1
            vals['seq_num'] = seq

            # Determine form code using SOP code structure if possible
            # Standard pattern: BX.YY.ZZZZ.SAA-FF
            # If the SOP is in draft, code can be partial or based on building/dept
            sop_code = sop.code or f"{sop.building_code}.{sop.dept_code}.XXXX-XX"
            # Strip version from SOP code (take part before '-')
            sop_base_code = sop_code.split('-')[0]
            vals['code'] = f"{sop_base_code}.{vals['form_type']}{seq:02d}-{vals['edition_num']:02d}"

        return super().create(vals_list)

    def write(self, vals: dict[str, Any]) -> bool:
        """Prevent changing SOP or type if already set."""
        if 'sop_id' in vals or 'form_type' in vals:
            for record in self:
                raise UserError(_("Cannot modify Associated SOP or Form Type after creation."))
        return super().write(vals)
