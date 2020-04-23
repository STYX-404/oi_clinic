
from odoo import api, fields, models


class HealthReport(models.Model):
    _name = 'health.report'
    _description = 'this model is for Result of student health report'

    st_ids = fields.Many2many(comodel_name="students.data", column1="st_name", string="Student", )

    st_height = fields.Float(string="Height",  required=True, )
    st_weight = fields.Float(string="Weight",  required=True, )
    st_bmi = fields.Float(string="BMI",  required=False, compute="gen_bmi", )


    right_eye = fields.Char(string="Right", required=True, )
    left_eye = fields.Char(string="Left", required=True, )
    glasses = fields.Boolean(string="Has Glasses ?",  )


    breast_diseases = fields.Char(string="Breast Diseases", )
    blood_pressure = fields.Char(string="Blood Pressure",  required=True,)
    birth_defect = fields.Char(string="Birth Defect and Impairments", )


    drugs = fields.Boolean(string="Drug Analysis",  )
    result = fields.Selection(string="Result", selection=[('p', 'Positive'), ('n', 'Negative'), ], required=False, default='n', )
    type_drug = fields.Char(string="Type of Drugs", required=False, )


    st_notes = fields.Text(string="Notes", required=False, )


    accept_unaccept = fields.Selection(string="Acceptable or Not", selection=[('ac', 'Acceptable'), ('un', 'Unacceptable'), ], required=True, default='un',)


    lab_info = fields.Many2one(comodel_name="lab.reports", string="Laboratory",  )
    he_value = fields.Float(string="Hemoglobin - Hb %",)
    he_normal_value = fields.Text(string="Normal Value", readonly=True, default="(12-16) mg/dl", )

    cl_value = fields.Float(string="Control", )
    cl_normal_value = fields.Text(string="Normal Value", readonly=True, default="12", )

    pt_value = fields.Float(string="Patient Time", )
    pt_normal_value = fields.Text(string="Normal Value", readonly=True, default="(12-16) Seconds", )

    co_value = fields.Float(string="Concentration", )
    co_normal_value = fields.Text(string="Normal Value", readonly=True, default="(70-100) %", )

    inr_value = fields.Float(string="INR", )
    inr_normal_value = fields.Text(string="Normal Value", readonly=True, default="(1-2)", )

    rbs_value = fields.Float(string="Random Blood Sugar", )
    rbs_normal_value = fields.Text(string="Normal Value", readonly=True, default="(60-160) mg/dl", )

    sc_value = fields.Float(string="S.Creatinine", )
    sc_normal_value = fields.Text(string="Normal Value", readonly=True, default="(0.6-1.5) mg/dl", )

    ur_value = fields.Float(string="Urea", )
    ur_normal_value = fields.Text(string="Normal Value", readonly=True, default="(15-45) mg/dl", )

    sg_value = fields.Float(string="S.GOT", )
    sg_normal_value = fields.Text(string="Normal Value", readonly=True, default="(5-45) U/I", )

    sgp_value = fields.Float(string="S.GPT", )
    sgp_normal_value = fields.Text(string="Normal Value", readonly=True, default="(5-45) U/I", )

    # ------------------- generate BMI ---------------------

    @api.multi
    @api.depends('st_weight', 'st_height')
    def gen_bmi(self):
        for record in self:

            if record.st_height >= 0.1:
                weight = record.st_weight
                height = record.st_height
                height_m = height / 100
                square_height = height_m * height_m
                bmi = weight / square_height
                record.st_bmi = bmi
            else:
                record.st_bmi = 0.0

