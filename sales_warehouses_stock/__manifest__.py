# -*- coding: utf-8 -*-
{
    'name': "Module custom",
    'summary': "Show warehouses and pricelist on  sale lines",
    'description': "Show warehouses and pricelist on  sale lines",
    'author': "Gustavo H.",
    'category': 'Sales/Sales',
    'version': '1.0',
    'depends': ['base', 'web', 'stock', 'sale_stock'],
    'qweb': [
        'static/src/xml/qty_at_date.xml'
    ],
    'data': [
        'views/stock_warehouse_view.xml',
        'views/sale_order_views.xml',
    ],
}