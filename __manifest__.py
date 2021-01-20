# -*- coding: utf-8 -*-
{
    'name': "Partner Master Extension",

    'summary': """
        Adding extra fields in Partner master and sale order""",

    'description': """
        1. New ref fields
    """,

    'author': "Bista Solutions",
    'website': "http://www.bistasolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/security.xml',

        'data/ir_sequence_data.xml',
        'data/mail_template_data_inherit.xml',

        'views/res_partner_views.xml',
        'views/purchase_views.xml',
        'views/account_move_views.xml',
        'views/sale_views.xml',
        'views/account_invoice_report_view.xml',

        'report/sale_report_inherit.xml',
        'report/invoice_report_inherit.xml',
        'report/custom_sale_report.xml',
        'report/custom_sale_report_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
