
from odoo import models, api, fields


class Employees(models.Model):
    _name = 'employees.data'
    _description = 'this model is for employees and professors data'

    e_image = fields.Binary(string="Add image",)
    e_job = fields.Selection(string="Employee job", selection=[('p', 'Professor'),
                                                               ('ta', 'Teaching assistant'),
                                                               ('l','Labor') ], required=True, )

    e_name = fields.Char(string="Name", required=True, )
    e_phone = fields.Char(string="Phone number", required=False, )
    e_email = fields.Char(string="E-mail", required=False, )
    e_code = fields.Char(string="Employee code", required=False, )


    @api.model
    def create(self, values):
        values.update({"e_code": self.env["ir.sequence"].next_by_code("employees_code_num")})
        return super(Employees, self).create(values)

    @api.multi
    def write(self, values):
        return super(Employees, self).write(values)

