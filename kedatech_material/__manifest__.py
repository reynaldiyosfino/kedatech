# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Kedatech - Product Material',
    'version': '15.0.1.0.0',
    'category': 'Stock',
    'summary': 'Product Material for Kedatech',
    'description': """
    v.1.0 (Rey) \n
    - Product Material for Kedatech\n
    """,
    'author': 'Reynaldi Yosfino',
    'images': [],
    'depends': [
        'base', 'contacts'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_material_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}
