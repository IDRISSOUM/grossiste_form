# -*- coding: utf-8 -*-
{
    'name': "gossiste_open",

    'summary': """
        Formulaire pour l'enroulement des grossiste """,

    'description': """
        Long description of module's purpose
    """,

    'author': "ben Marzouk",
    'website': "moise.groupecerco.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'mail'],

    # always loaded
    'data': [
        'security/grossiste_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/website_form.xml',
        'views/category_type.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
