# -*- coding: utf-8 -*-
from __future__ import annotations

from typing import Any
from odoo import api, fields, models, _
from odoo.exceptions import AccessError

class ResUsers(models.Model):
    _inherit = 'res.users'

    def check_pending_training_compliance(self) -> None:
        """Check if the user has any overdue pending training records.
        If yes, raises an AccessError to restrict actions.
        """
        self.ensure_one()
        # Bypass admin to prevent locking the configuration panel
        if self._is_admin():
            return

        # Search active plans containing pending training records for this user
        pending_records = self.env['qms.sop.training.record'].search([
            ('user_id', '=', self.id),
            ('state', '=', 'pending'),
            ('plan_id.state', '=', 'active'),
        ])

        # Filter records where training deadline is overdue
        overdue_records = pending_records.filtered(
            lambda r: r.plan_id.deadline and r.plan_id.deadline < fields.Date.context_today(self)
        )

        if overdue_records:
            sop_names = ", ".join(overdue_records.mapped('sop_id.name'))
            raise AccessError(_(
                "Đăng nhập bị từ chối: Bạn có lịch đào tạo SOP quá hạn chưa hoàn thành cho các quy trình sau: %s. "
                "Vui lòng hoàn thành đào tạo và báo với Training Coordinator để được kích hoạt tài khoản.",
                sop_names
            ))

    def _check_credentials(self, credential, env):
        """Override _check_credentials to enforce training checks on user login."""
        result = super()._check_credentials(credential, env)
        # self.env.user refers to the user attempting login
        try:
            self.env.user.check_pending_training_compliance()
        except AccessError as e:
            from odoo.exceptions import AccessDenied
            raise AccessDenied(e.args[0]) from e
        return result
