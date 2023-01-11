# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalPatient(http.Controller):
#     @http.route('/hospital_patient/hospital_patient', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_patient/hospital_patient/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_patient.listing', {
#             'root': '/hospital_patient/hospital_patient',
#             'objects': http.request.env['hospital_patient.hospital_patient'].search([]),
#         })

#     @http.route('/hospital_patient/hospital_patient/objects/<model("hospital_patient.hospital_patient"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_patient.object', {
#             'object': obj
#         })
