import base64
from odoo import models, api, fields
from odoo.odoo.modules.module import get_module_resource
from odoo.odoo import tools

class Students(models.Model):
    _name = 'students.data'
    _rec_name = 'st_code'
    _description = 'the Students model is used for adding new students and there information to the database.'


    @api.model
    def _default_image(self):
        image_path = get_module_resource('hr', 'static/src/img', 'default_image.png')
        return tools.image_resize_image_big(base64.b64encode(open(image_path, 'rb').read()))

    st_name = fields.Char(string="Name", required=True,)
    st_code = fields.Char(string="Student code", required=False, readonly=True, )
    st_major = fields.Selection(string="Major", selection=[('cs', 'Computer science'),
                                                                   ('is', 'Information systems'),
                                                                   ('ba', 'Business administration')], required=True, )

    st_academic_year = fields.Selection(string="Academic year", selection=[('1st', 'First year'),
                                                              ('2nd', 'Second year'),
                                                              ('3rd', 'Third year'),
                                                              ('4th', 'Fourth year')], required=True, )
    st_email = fields.Char(string="E-mail", required=False, compute="gen_email")
    st_password = fields.Char(string="Password", required=True, compute="gen_password")
    st_phone = fields.Char(string="Phone number", required=True, )
    st_address = fields.Char(string="Address", required=True, )

    image = fields.Binary("Photo", default=_default_image, attachment=True,)
    image_medium = fields.Binary("Medium-sized photo", attachment=True,)
    image_small = fields.Binary("Small-sized photo", attachment=True,)

    # ------------------- generate student code ---------------------

    @api.model
    def create(self, values):
        values.update({"st_code": self.env["ir.sequence"].next_by_code("students_code_num")})
        return super(Students, self).create(values)

    @api.multi
    def write(self, values):
        return super(Students, self).write(values)

    # ------------------- generate email ---------------------

    @api.multi
    @api.depends('st_name', 'st_code')
    def gen_email(self):
        for record in self:
            domain = "@oi.edu.eg"
            name = record.st_name.__str__().split(" ")
            id = record.st_code.__str__()
            if name.__len__() >= 2:
                unique_name = name[0] + "_" + name[1]
                record.st_email = unique_name + "_" + id + domain
            else:
                unique_name = name[0]
                record.st_email = unique_name + "_" + id + domain

    # ------------------- generate email password ---------------------

    @api.multi
    @api.depends('st_name', 'st_code', 'st_phone')
    def gen_password(self):
        for record in self:
            name = record.st_name.__str__()
            id = record.st_code.__str__()
            phone_num = record.st_phone.__str__()
            record.st_password = name[0]+name[1] + id + phone_num[-2] + phone_num[-1]