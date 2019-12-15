from odoo import models, api, fields


class DocsAndNurses(models.Model):
    _name = 'docsAndNurses.data'
    _description = 'this model is for employees and professors data'

    docsAndNurses_image = fields.Binary(string="Add image",)
    docsAndNurses_job = fields.Selection(string="job", selection=[('d', 'Doctor'),
                                                                  ('n', 'Nurse')], required=True, )

    docsAndNurses_name = fields.Char(string="Name", required=True, )
    docsAndNurses_phone = fields.Char(string="Phone number", required=False, )
    docsAndNurses_code = fields.Char(string="code", required=False, )


    @api.model
    def create(self, values):
        values.update({"docsAndNurses_code": self.env["ir.sequence"].next_by_code("docsAndNurses_code_num")})
        return super(DocsAndNurses, self).create(values)

    @api.multi
    def write(self, values):
        return super(DocsAndNurses, self).write(values)

