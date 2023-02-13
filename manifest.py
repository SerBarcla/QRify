{
    'name': "QRify",
    'summary': "Turn Odoo records into QR codes",
    'description': "This module allows you to turn any Odoo record into a QR code, which can be scanned to open the concerned record.",
    'category': 'Tools',
    'version': '12.0.1.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/qrify_views.xml',
    ],
    'installable': True,
    'application': True,
}
