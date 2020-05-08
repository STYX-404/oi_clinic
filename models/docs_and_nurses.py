from odoo import models, api, fields
from odoo.exceptions import UserError, ValidationError


class Doctors(models.Model):
    _name = 'doctors.data'
    _rec_name = 'doctors_name'
    _description = 'this model is for employees and professors data'

    doctors_image = fields.Binary(string="Photo",)
    doctors_job = fields.Selection(string="Job", selection=[('d', 'Doctor'),
                                                            ('n', 'Nurse')], required=True, )

    doctors_name = fields.Char(string="Name", required=True, )
    doctors_phone = fields.Char(string="Phone number", required=True, )
    doctors_code = fields.Char(string="Code", required=False, readonly=True )




    @api.model
    def create(self, values):
        values.update({"doctors_code": self.env["ir.sequence"].next_by_code("doctors_code_num")})
        return super(Doctors, self).create(values)

    @api.multi
    def write(self, values):
        return super(Doctors, self).write(values)

        # ------------------- Check phone Number ---------------------
    @api.multi
    @api.constrains('doctors_phone')
    def _check_phone_number(self):

        for rec in self:

            phone = rec.doctors_phone.__str__()

            if phone.__len__() != 11:

                raise ValidationError("Invalid Phone Number")

            else:
                return False

        # ------------------- Check Name ---------------------
    @api.multi
    @api.constrains('doctors_name')
    def _check_name(self):

        for rec in self:

            name = rec.doctors_name.__str__().split(" ")

            if name.__len__() >= 2:

                return False

            else:
                raise ValidationError("Enter Full Name")


