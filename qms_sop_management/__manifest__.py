# -*- coding: utf-8 -*-
{
    'name': 'QMS SOP & Document Control',
    'version': '19.0.1.0.0',
    'category': 'Quality',
    'summary': 'Manage Standard Operating Procedures (SOP), Forms, Logbooks and GMP Compliance Training',
    'description': """
Quality Management System (QMS) - Document Control and SOP Lifecycle Management:
- SOP lifecycle (Draft, Review, Approve, Training, Effective, Obsolete).
- Automatic document numbering customization.
- Issuing and tracking of controlled copies, reference copies, forms, and logbooks.
- Standard training tracking & compliance restrictions.
- Spell correction requests and document loss reports.
    """,
    'author': 'Antigravity Odoo AI Agent',
    'license': 'LGPL-3',
    'depends': ['base', 'mail', 'hr'],
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'security/qms_security_rules.xml',
        'data/qms_cron_data.xml',
        'views/qms_change_control_views.xml',
        'views/qms_sop_views.xml',
        'views/qms_sop_form_views.xml',
        'views/qms_sop_logbook_views.xml',
        'views/qms_sop_distribution_views.xml',
        'views/qms_training_views.xml',
        'views/qms_sop_loss_views.xml',
        'views/qms_sop_spell_views.xml',
        'views/menu_items.xml',
        'reports/qms_sop_reports.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
