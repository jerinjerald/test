# -*- coding: utf-8 -*-
{
    'name': "SW - Barcode Column",

    'summary': """
    This module adds a new column [Barcode] at SO, DO, INV, 
    and PO and adds a sequence number to the line items and the printed reports
    """,
    'description': """
    This module adds a new column [Barcode] at SO, DO, INV,
     and PO and adds a sequence number to the line items and the printed reports
    """,
    'author': "",
    'website': "",
    'category': '',
    'version': '12.0.1.1',
    'depends': ['base','sale','purchase','stock','account','order_line_sequence'],
    'data': [
        'views/barcode_column.xml',
        'template/sale_order_template.xml',
        'template/purchase_rder_template.xml',
       
        'template/picking_operation.xml'
    ],
}
