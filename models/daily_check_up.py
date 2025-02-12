
from odoo import models, api, fields

class StudentsCheckUp(models.Model):
    _name = 'stdailycheckup.data'
    _rec_name = 'stu_ids'
    _description = 'This model is used for daily check-up for students'

    stu_ids = fields.Many2one(comodel_name="students.data", string="Student", required=True,)
    stu_nurse = fields.Many2one(comodel_name="doctors.data", string="Nurse", required=True, domain=[('doctors_job','=','n')],)
    stu_doctor = fields.Many2one(comodel_name="doctors.data", string="Doctor", required=True, domain=[('doctors_job','=','d')],)
    stu_diagnosis = fields.Text(string="Diagnosis", required=True, )
    stu_date = fields.Datetime(string="Date", default=fields.Datetime.now(),)
    med_ids = fields.Many2one(comodel_name="medicines.data", string="Medicine", required=True, )
    med_dose = fields.Integer(string="Dose", required=True, default=1, )
    another_med = fields.Boolean(string="Take Another Medicine",  )
    med_ids_2 = fields.Many2one(comodel_name="medicines.data", string="Medicine", required=False, )
    med_dose_2 = fields.Integer(string="Dose", required=False, default=0, )

    @api.onchange('stu_diagnosis')
    def update_date(self):
        for rec in self:
            if rec.stu_diagnosis:
                rec.stu_date = fields.Datetime.now()


class EmployeeCheckUp(models.Model):
    _name = 'emdailycheckup.data'
    _rec_name = 'em_ids'
    _description = 'This model is used for daily check-up for professors and employees'

    em_ids = fields.Many2one(comodel_name="employees.data", string="Employee", required=True )
    em_doctor = fields.Many2one(comodel_name="doctors.data", string="Doctor", required=True, domain=[('doctors_job','=','d')], )
    em_diagnosis = fields.Text(string="Diagnosis", required=True, )
    em_date = fields.Datetime(string="Date", default=fields.Datetime.now(),)
    med_ids = fields.Many2one(comodel_name="medicines.data", string="Medicine", required=True, )
    med_dose = fields.Integer(string="Dose", required=True, default=1, )
    another_med = fields.Boolean(string="Take Another Medicine", )
    med_ids_2 = fields.Many2one(comodel_name="medicines.data", string="Medicine", required=False, )
    med_dose_2 = fields.Integer(string="Dose", required=False, default=0, )

    @api.onchange('em_diagnosis')
    def update_date(self):
        for rec in self:
            if rec.em_diagnosis:
                rec.em_date = fields.Datetime.now()

    # @api.multi
    # @api.depends('med_dose', 'med_ids', )
    # @api.onchange('med_dose')
    # def update_stock(self):
    #
    #     global emp_med_name, dose, stock, medicine_name
    #     get_stock = self.env["medicines.data"].search([])
    #     for record in self:
    #         emp_med_name = record.med_ids.med_name
    #         dose = record.med_dose
    #         for item in get_stock:
    #             stock = item.med_stock
    #             medicine_name = item.med_name
    #             if medicine_name == emp_med_name:
    #                 print(medicine_name, stock, emp_med_name, dose )
    #                 item.med_stock -= record.med_dose
