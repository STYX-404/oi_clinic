
from odoo import models, api, fields


class StudentsFollowUp(models.Model):
    _name = 'medicalfollowup.data'
    _description = 'This model is used for medical follow-up for students, professors and employees'

    stu_ids = fields.Many2many(comodel_name="students.data", column1="st_code", column2="st_name", string="Student Information", )
    diagnosis = fields.Text(string="Diagnosis", required=True, )
    doctor_id = fields.Many2one(comodel_name="doctors.data", string="Doctor", required=True, )
    nurse_id = fields.Many2one(comodel_name="doctors.data", string="Nurse", required=True, )
    em_ids = fields.Many2many(comodel_name="employees.data", column1="e_name", column2="e_code", string="Doctor Or Employee Information", )
    date = fields.Date(string="Date", default=fields.Date.today(), )



