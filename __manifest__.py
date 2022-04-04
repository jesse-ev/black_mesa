# -*- coding: utf-8 -*-
{
    'name': "Black mesa manufacturing",

    'summary': """
        A pseudo-manufacturing system for Black Mesa""",

    'description': """
        This module is created for training purpose, this module serves as custom-module making assignment for internship.
    """,

    'author': "Je-Bot Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.1',
    'application':True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/material_views.xml',
        'views/staff_scientist_views.xml',
        'views/build_views.xml',
        'views/staff_security_views.xml',
        'views/staff_engineer_views.xml',
        'views/workspace_views.xml',
        'views/inventory_views.xml',
        'report/report.xml',
        'report/inventory.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
