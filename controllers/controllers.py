# -*- coding: utf-8 -*-
# from odoo import http


# class Checkin(http.Controller):
#     @http.route('/checkin/checkin/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/checkin/checkin/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('checkin.listing', {
#             'root': '/checkin/checkin',
#             'objects': http.request.env['checkin.checkin'].search([]),
#         })

#     @http.route('/checkin/checkin/objects/<model("checkin.checkin"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('checkin.object', {
#             'object': obj
#         })
