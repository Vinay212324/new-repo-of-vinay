{
    'name': 'Registration Form new',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Module to manage register forms',
    'description': 'This module provides a model to manage register forms.',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/reg_form.xml',
    ],
    'installable': True,
    'application': True,
}
