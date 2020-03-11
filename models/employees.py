import base64

from odoo import api, fields, models

from odoo.odoo import tools, _
from odoo.odoo.exceptions import ValidationError, AccessError
from odoo.odoo.modules.module import get_module_resource

class Employees(models.Model):
    _name = 'employees.data'
    _description = 'this model is for employees and professors data'
    #


    @api.model
    def _default_image(self):
        image_path = get_module_resource('hr', 'static/src/img', 'default_image.png')
        return tools.image_resize_image_big(base64.b64encode(open(image_path, 'rb').read()))

    # e_image = fields.Binary(string="Add image",)
    e_job = fields.Selection(string="Employee job", selection=[('p', 'Professor'),
                                                               ('ta', 'Teaching assistant'),
                                                               ('l','Labor') ], required=True, )

    e_name = fields.Char(string="Name", required=True, )
    e_phone = fields.Char(string="Phone number", required=False, )
    e_email = fields.Char(string="E-mail", required=False, )
    e_code = fields.Char(string="Employee code", required=False, )
    e_notes = fields.Text('Notes')
    passport_id = fields.Char('Passport No',)
    national_id = fields.Char(string='National Id No',)
    bank_account_id = fields.Char(string="Bank Account Number", required=False, )
    permit_no = fields.Char('Work Permit No', )
    visa_no = fields.Char('Visa No', )
    visa_expire = fields.Date('Visa Expire Date', )
    additional_note = fields.Text(string='Additional Note',)
    country_id = fields.Many2one(
        'res.country', 'Nationality (Country)',)
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

    image = fields.Binary(
        "Photo", default=_default_image, attachment=True,
        help="This field holds the image used as photo for the employee, limited to 1024x1024px.")
    image_medium = fields.Binary(
        "Medium-sized photo", attachment=True,
        help="Medium-sized photo of the employee. It is automatically "
             "resized as a 128x128px image, with aspect ratio preserved. "
             "Use this field in form views or some kanban views.")
    image_small = fields.Binary(
        "Small-sized photo", attachment=True,
        help="Small-sized photo of the employee. It is automatically "
             "resized as a 64x64px image, with aspect ratio preserved. "
             "Use this field anywhere a small image is required.")


    @api.model
    def create(self, values):
        values.update({"e_code": self.env["ir.sequence"].next_by_code("employees_code_num")})
        return super(Employees, self).create(values)

    @api.multi
    def write(self, values):
        return super(Employees, self).write(values)
