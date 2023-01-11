# -*- coding: utf-8 -*-
{
    'name': "HospitalPatient",
    'summary': """
        this is a application of Hospitality 
        """,

    'description': """
        thisi is just testing 
    """,

    'author': "Mokhles Abdelmonem",
    'website': "http://www.facebook.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient.xml',
        'views/female_patient.xml',
        'views/appoinment.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'sequence': 0,
}
