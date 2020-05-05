from odoo import models, api, fields


class Doctors(models.Model):
    _name = 'doctors.data'
    _rec_name = 'doctors_name'
    _description = 'this model is for employees and professors data'

    doctors_image = fields.Binary(string="Add image",)
    doctors_job = fields.Selection(string="Job", selection=[('d', 'Doctor'),
                                                            ('n', 'Nurse')], required=True, )

    doctors_name = fields.Char(string="Name", required=True, )
    doctors_phone = fields.Char(string="Phone number", required=False, )
    doctors_code = fields.Char(string="Code", required=False, )




    @api.model
    def create(self, values):
        values.update({"doctors_code": self.env["ir.sequence"].next_by_code("doctors_code_num")})
        return super(Doctors, self).create(values)

    @api.multi
    def write(self, values):
        return super(Doctors, self).write(values)

