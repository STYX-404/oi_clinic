
from odoo import api, fields, models

class Laboratory(models.Model):
    _name = 'lab.reports'
    _rec_name = 'lab_name'
    _description = 'this model is for Result of Blood Testing'


    lab_name = fields.Char(string="Name", required=True, )

    lab_branch = fields.Text(string="Address", required=True, )
    lab_phone = fields.Char(string="Phone", required=True, )
    another_phone = fields.Boolean(string="Add another phone", )
    second_phone = fields.Char(string="Another phone", required=False, )
    another_branch= fields.Boolean(string="Add another Branch",  )
    sec_branch = fields.Text(string="Address", required=False, )
    sec_branch_num = fields.Char(string="Phone", required=False, )
    another_phone_sec_branch = fields.Boolean(string="Add another phone",  )
    sec_phone_sec_branch = fields.Char(string="Another phone", required=False, )
    lab_image = fields.Binary(string="Photo", )
    lab_id = fields.Char(string="Laboratory Id", required=False, readonly=True, )

    @api.model
    def create(self, values):
        values.update({"lab_id": self.env["ir.sequence"].next_by_code("lab_id_num")})
        return super(Laboratory, self).create(values)

    @api.multi
    def write(self, values):
        return super(Laboratory, self).write(values)