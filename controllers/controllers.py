# -*- coding: utf-8 -*-
from odoo import http

# class OiClinic(http.Controller):
#     @http.route('/oi_clinic/oi_clinic/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oi_clinic/oi_clinic/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oi_clinic.listing', {
#             'root': '/oi_clinic/oi_clinic',
#             'objects': http.request.env['oi_clinic.oi_clinic'].search([]),
#         })

#     @http.route('/oi_clinic/oi_clinic/objects/<model("oi_clinic.oi_clinic"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oi_clinic.object', {
#             'object': obj
#         })