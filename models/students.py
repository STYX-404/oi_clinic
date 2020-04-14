
from odoo import models, api, fields


class Students(models.Model):
    _name = 'students.data'
    _rec_name = 'st_name'
    _description = 'the Students model is used for adding new students and there information to the database.'

    st_name = fields.Char(string="Student name", required=True, )
    st_code = fields.Char(string="Student code", required=False, readonly=True, )
    st_major = fields.Selection(string="Major", selection=[('cs', 'Computer science'),
                                                                   ('is', 'Information systems'),
                                                                   ('ba', 'Business administration')], required=True, )

    st_academic_year = fields.Selection(string="Academic year", selection=[('1st', 'First year'),
                                                              ('2nd', 'Second year'),
                                                              ('3rd', 'Third year'),
                                                              ('4th', 'Fourth year')], required=True, )

    @api.model
    def create(self, values):
        values.update({"st_code": self.env["ir.sequence"].next_by_code("students_code_num")})
        return super(Students, self).create(values)

    @api.multi
    def write(self, values):
        return super(Students, self).write(values)