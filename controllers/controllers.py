# -*- coding: utf-8 -*-
# from odoo import http


# class EmptyBoilerplate(http.Controller):
#     @http.route('/empty_boilerplate/empty_boilerplate/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/empty_boilerplate/empty_boilerplate/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('empty_boilerplate.listing', {
#             'root': '/empty_boilerplate/empty_boilerplate',
#             'objects': http.request.env['empty_boilerplate.empty_boilerplate'].search([]),
#         })

#     @http.route('/empty_boilerplate/empty_boilerplate/objects/<model("empty_boilerplate.empty_boilerplate"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('empty_boilerplate.object', {
#             'object': obj
#         })
