import base64
from odoo import api, fields, models
from odoo.odoo.modules.module import get_module_resource
from odoo.odoo import tools
class Employees(models.Model):
    _name = 'employees.data'
    _rec_name = 'e_name'
    _description = 'this model is for employees and professors data'

    @api.model
    def _default_image(self):
        image_path = get_module_resource('hr', 'static/src/img', 'default_image.png')
        return tools.image_resize_image_big(base64.b64encode(open(image_path, 'rb').read()))

    e_job = fields.Selection(string="Employee job", selection=[('p', 'Professor'),
                                                               ('ta', 'Teaching assistant'),
                                                               ('l','Labor') ], required=True, )

    e_name = fields.Char(string="Name", required=True, )
    e_phone = fields.Char(string="Phone number", required=True, )
    e_email = fields.Char(string="E-mail", required=False, compute="gen_email")
    e_password = fields.Char(string="Password", required=True, compute="gen_password")
    e_code = fields.Char(string="Employee code", required=False, readonly=True)
    e_notes = fields.Text('Notes')
    passport_id = fields.Char('Passport No',)
    national_id = fields.Char(string='National Id No',)
    bank_account_id = fields.Char(string="Bank Account Number", required=False, )
    permit_no = fields.Char('Work Permit No', )
    visa_no = fields.Char('Visa No', )
    visa_expire = fields.Date('Visa Expire Date', )
    additional_note = fields.Text(string='Additional Note',)
    country_id = fields.Many2one('res.country', 'Nationality (Country)',)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], default="male")
    marital = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('cohabitant', 'Legal Cohabitant'),
        ('widower', 'Widower'),
        ('divorced', 'Divorced')
    ], string='Marital Status' , default='single')

    children = fields.Integer(string='Number of Children', )
    place_of_birth = fields.Char('Place of Birth', )
    country_of_birth = fields.Many2one('res.country', string="Country of Birth", )
    birthday = fields.Date('Date of Birth', )
    ssnid = fields.Char('SSN No', help='Social Security Number', )
    sinid = fields.Char('SIN No', help='Social Insurance Number', )
    study_field = fields.Char("Field of Study", placeholder='Computer Science',)
    study_school = fields.Char("School",)
    emergency_contact = fields.Char("Emergency Contact", )
    emergency_phone = fields.Char("Emergency Phone", )
    certificate = fields.Selection([
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('Doctorate', 'Doctorate'),
        ('Secondary school', 'Secondary school'),
        ('primary school', 'primary school'),
        ('Not educated', 'Not educated'),
    ], 'Certificate Level', default='master',)

    image = fields.Binary("Photo", default=_default_image, attachment=True,)
    image_medium = fields.Binary("Medium-sized photo", attachment=True,)
    image_small = fields.Binary("Small-sized photo", attachment=True,)


    @api.model
    def create(self, values):
        values.update({"e_code": self.env["ir.sequence"].next_by_code("employees_code_num")})
        return super(Employees, self).create(values)

    @api.multi
    def write(self, values):
        return super(Employees, self).write(values)

    # ------------------- generate email ---------------------

    @api.multi
    @api.depends('e_name', 'e_code')
    def gen_email(self):
        for record in self:
            domain = "@oi.edu.eg"
            name = record.e_name.__str__().split(" ")
            id = record.e_code.__str__()
            if name.__len__() >= 2:
                unique_name = name[0] + "_" + name[1]
                record.e_email = unique_name + "_" + id + domain
            else:
                unique_name = name[0]
                record.e_email = unique_name + "_" + id + domain

    # ------------------- generate email password ---------------------

    @api.multi
    @api.depends('e_name', 'e_code', 'e_phone')
    def gen_password(self):
        for record in self:
            name = record.e_name.__str__()
            id = record.e_code.__str__()
            phone_num = record.e_phone.__str__()
            record.e_password = name[0] + name[1] + id + phone_num[-2] + phone_num[-1]
