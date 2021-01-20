# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerExtension(http.Controller):
#     @http.route('/partner_extension/partner_extension/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_extension/partner_extension/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_extension.listing', {
#             'root': '/partner_extension/partner_extension',
#             'objects': http.request.env['partner_extension.partner_extension'].search([]),
#         })

#     @http.route('/partner_extension/partner_extension/objects/<model("partner_extension.partner_extension"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_extension.object', {
#             'object': obj
#         })
