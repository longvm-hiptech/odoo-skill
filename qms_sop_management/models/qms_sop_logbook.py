# -*- coding: utf-8 -*-
from __future__ import annotations

from typing import Any, Optional
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class QmsSopLogbook(models.Model):
    _name = 'qms.sop.logbook'
    _description = 'QMS SOP Associated Logbook'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'code desc'
    _check_company_auto = True

    name: str = fields.Char(
        string='Logbook Name',
        required=True,
        tracking=True,
    )
    code: str = fields.Char(
        string='Logbook Code',
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
    page_count: int = fields.Integer(
        string='Page Count',
        required=True,
        default=100,
        tracking=True,
    )
    seq_num: int = fields.Integer(
        string='Logbook Sequence (AA)',
        readonly=True,
        copy=False,
    )
    edition_num: int = fields.Integer(
        string='Logbook Version (FF)',
        default=1,
        readonly=True,
        copy=False,
    )
    state: str = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('active', 'Active (In Use)'),
            ('closed', 'Closed'),
            ('recalled', 'Recalled'),
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

    @api.constrains('page_count')
    def _check_page_count(self) -> None:
        """Validate page count is positive."""
        for record in self:
            if record.page_count <= 0:
                raise ValidationError(_("Page count must be greater than zero."))

    @api.model_create_multi
    def create(self, vals_list: list[dict[str, Any]]) -> QmsSopLogbook:
        """Create logbook and auto-generate code."""
        for vals in vals_list:
            sop = self.env['qms.sop'].browse(vals['sop_id'])
            
            # Find max logbook sequence number (AA) for the same SOP
            domain = [
                ('sop_id', '=', vals['sop_id']),
                ('seq_num', '>', 0),
            ]
            existing_logbooks = self.search(domain, order='seq_num desc', limit=1)
            seq = (existing_logbooks.seq_num + 1) if existing_logbooks else 1
            vals['seq_num'] = seq

            # Determine logbook code using SOP code structure
            # Pattern: BX.YY.ZZZZ.LAA-FF (where L stands for logbook)
            sop_code = sop.code or f"{sop.building_code}.{sop.dept_code}.XXXX-XX"
            sop_base_code = sop_code.split('-')[0]
            vals['code'] = f"{sop_base_code}.L{seq:02d}-{vals['edition_num']:02d}"

        return super().create(vals_list)

    def write(self, vals: dict[str, Any]) -> bool:
        """State validation for closed/recalled states."""
        if 'state' in vals:
            for record in self:
                if vals['state'] == 'active' and record.state != 'draft':
                    raise UserError(_("Can only activate draft logbooks."))
        return super().write(vals)

    def action_activate(self) -> None:
        """Set logbook to Active."""
        self.write({'state': 'active'})

    def action_close(self) -> None:
        """Set logbook to Closed."""
        self.write({'state': 'closed'})

    def action_recall(self) -> None:
        """Set logbook to Recalled."""
        self.write({'state': 'recalled'})
