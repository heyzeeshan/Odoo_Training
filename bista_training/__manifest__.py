# -*- coding: utf-8 -*-
{
    'name': "Bista Training Management System",

    'summary': """
        Learn and experiment with new ideas""",

    'description': """
        1. Learn to build modules
        2. Experiment with new field, features, attributes etc
    """,

    'author': "Bista Solutions",
    'website': "http://www.bistasolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/training_view.xml',
        'views/trainee_view.xml',
        'views/trainer_view.xml',
        'views/location_view.xml',
        'views/designation_view.xml',
        'views/subjects_view.xml',
        'views/topics_view.xml',
        'views/templates.xml',
        'views/menu_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
