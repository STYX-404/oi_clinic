from odoo import api, fields, models

class Laboratory(models.Model):
    _name = 'lab.reports'
    _description = 'this model is for Result of Blood Testing'


    st_ids = fields.Many2many(comodel_name="students.data", column1="st_name", column2="st_code", string="Student", )


    he_value = fields.Float(string="Hemoglobin - Hb %", required=True, )
    he_normal_value = fields.Text(string="Normal Value", readonly=True, default="(12-16) mg/dl", )

    cl_value = fields.Float(string="Control", required=True, )
    cl_normal_value = fields.Text(string="Normal Value", readonly=True, default="12", )

    pt_value = fields.Float(string="Patient Time", required=True, )
    pt_normal_value = fields.Text(string="Normal Value", readonly=True, default="(12-16) Seconds", )

    co_value = fields.Float(string="Concentration", required=True, )
    co_normal_value = fields.Text(string="Normal Value", readonly=True, default="(70-100) %", )

    inr_value = fields.Float(string="INR", required=True, )
    inr_normal_value = fields.Text(string="Normal Value", readonly=True, default="(1-2)", )

    rbs_value = fields.Float(string="Random Blood Sugar", required=True, )
    rbs_normal_value = fields.Text(string="Normal Value", readonly=True, default="(60-160) mg/dl", )

    sc_value = fields.Float(string="S.Creatinine", required=True, )
    sc_normal_value = fields.Text(string="Normal Value", readonly=True, default="(0.6-1.5) mg/dl", )

    ur_value = fields.Float(string="Urea", required=True, )
    ur_normal_value = fields.Text(string="Normal Value", readonly=True, default="(15-45) mg/dl", )

    sg_value = fields.Float(string="S.GOT", required=True, )
    sg_normal_value = fields.Text(string="Normal Value", readonly=True, default="(5-45) U/I", )

    sgp_value = fields.Float(string="S.GPT", required=True, )
    sgp_normal_value = fields.Text(string="Normal Value", readonly=True, default="(5-45) U/I", )




