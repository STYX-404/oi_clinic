
from odoo import models, api, fields


class StudentsFollowUp(models.Model):
    _name = 'medicalfollowup.data'
    _description = 'This model is used for medical follow-up for students, professors and employees'

    stu_ids = fields.Many2many(comodel_name="students.data", column1="st_name", column2="st_code", string="Student", )
    stu_nurse = fields.Many2one(comodel_name="doctors.data", string="Nurse", required=True, )
    stu_doctor = fields.Many2one(comodel_name="doctors.data", string="Doctor", required=True, )
    stu_diagnosis = fields.Text(string="Diagnosis", required=True, )
    stu_date = fields.Date(string="Date", required=fields.Date.today(), )
    em_ids = fields.Many2many(comodel_name="employees.data", column1="e_name", column2="e_code", string="Employee", )
    em_doctor = fields.Many2one(comodel_name="doctors.data", string="Doctor", required=True, )
    em_diagnosis = fields.Text(string="Diagnosis", required=True, )
    em_date = fields.Date(string="Date", required=fields.Date.today(), )







