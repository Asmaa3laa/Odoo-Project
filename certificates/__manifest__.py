# -*- coding: utf-8 -*-
{
    'name': "alnoor certificates",
    'description': """

     """,
    'depends': [],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'reports/report.xml',
        'reports/report_certificate_template.xml',
        'views/certificate_type_views.xml',
        'views/certificate_views.xml',
        'views/customer_views.xml',
        'views/expenses_views.xml',
        'data/ir_sequence.xml'
    ],
    'installable': True,
    'auto_install': False,
    'sequence': 1,
    'assets': {
        'web.report_assets_common': [
            '/certificates/static/src/css/report_styles.css',
        ],
    },
}
