
from odoo import models, api, fields


class StudentsFollowUp(models.Model):
    _name = 'stmedicalfollowup.data'
    _description = 'This model is used for medical follow-up for students'

    stu_id = fields.Many2one(comodel_name="students.data", string="Student", required=True,)
    stu_nurse = fields.Many2one(comodel_name="doctors.data", string="Nurse", required=True, )
    stu_doctor = fields.Many2one(comodel_name="doctors.data", string="Doctor", required=True, )
    stu_diagnosis = fields.Text(string="Diagnosis", required=True, )
    stu_date = fields.Date(string="Date", required=fields.Date.today(), )



class EmployeeFollowUp(models.Model):
    _name = 'emmedicalfollowup.data'
    _description = 'This model is used for medical follow-up for professors and employees'

    em_id = fields.Many2one(comodel_name="employees.data", string="Employee", required=True )
    em_doctor = fields.Many2one(comodel_name="doctors.data", string="Doctor", required=True, )
    em_diagnosis = fields.Text(string="Diagnosis", required=True, )
    em_date = fields.Date(string="Date", required=fields.Date.today(), )


