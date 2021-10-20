# -*- coding: utf-8 -*-
# from odoo import http


# class ListPricePercent(http.Controller):
#     @http.route('/list_price_percent/list_price_percent/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/list_price_percent/list_price_percent/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('list_price_percent.listing', {
#             'root': '/list_price_percent/list_price_percent',
#             'objects': http.request.env['list_price_percent.list_price_percent'].search([]),
#         })

#     @http.route('/list_price_percent/list_price_percent/objects/<model("list_price_percent.list_price_percent"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('list_price_percent.object', {
#             'object': obj
#         })
