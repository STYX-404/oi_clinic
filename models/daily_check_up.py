
from odoo import models, api, fields


class StudentsFollowUp(models.Model):
    _name = 'stdailycheckup.data'
    _rec_name = 'stu_doctor'
    _description = 'This model is used for daily check-up for students'

    stu_ids = fields.Many2many(comodel_name="students.data", string="Student", required=True,)
    stu_nurse = fields.Many2one(comodel_name="doctors.data", string="Nurse", required=True, domain=[('doctors_job','=','n')],)
    stu_doctor = fields.Many2one(comodel_name="doctors.data", string="Doctor", required=True, domain=[('doctors_job','=','d')],)
    stu_diagnosis = fields.Text(string="Diagnosis", required=True, )
    stu_date = fields.Datetime(string="Date", default=fields.Datetime.now(), readonly=True, )

class EmployeeFollowUp(models.Model):
    _name = 'emdailycheckup.data'
    _rec_name = 'em_doctor'
    _description = 'This model is used for daily check-up for professors and employees'

    em_ids = fields.Many2many(comodel_name="employees.data", string="Employee", required=True )
    em_doctor = fields.Many2one(comodel_name="doctors.data", string="Doctor", required=True, domain=[('doctors_job','=','d')], )
    em_diagnosis = fields.Text(string="Diagnosis", required=True, )
    em_date = fields.Datetime(string="Date", default=fields.Datetime.now(), readonly=True, )

