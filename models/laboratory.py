from odoo import api, fields, models

class Laboratory(models.Model):
    _name = 'lab.reports'
    _description = 'this model is for Result of Blood Testing'


    st_ids = fields.Many2many(comodel_name="students.data", column1="st_name", column2="st_code", string="Student", )


    he_test_name = fields.Char(string="Test Name", readonly=True, default="Hemoglobin - Hb %",  )
    he_value = fields.Float(string="Value", required=True, )
    he_normal_value = fields.Text(string="Normal Value", readonly=True, default="(12-16) mg/dl", )

    cl_test_name = fields.Char(string="Test Name", readonly=True, default="Control",  )
    cl_value = fields.Float(string="Value", required=True, )
    cl_normal_value = fields.Text(string="Normal Value", readonly=True, default="12", )

    pt_test_name = fields.Char(string="Test Name", readonly=True, default="Patient Time", )
    pt_value = fields.Float(string="Value", required=True, )
    pt_normal_value = fields.Text(string="Normal Value", readonly=True, default="(12-16) Seconds", )

    co_test_name = fields.Char(string="Test Name", readonly=True, default="Concentration", )
    co_value = fields.Float(string="Value", required=True, )
    co_normal_value = fields.Text(string="Normal Value", readonly=True, default="(70-100) %", )

    inr_test_name = fields.Char(string="Test Name", readonly=True, default="INR", )
    inr_value = fields.Float(string="Value", required=True, )
    inr_normal_value = fields.Text(string="Normal Value", readonly=True, default="(1-2)", )

    rbs_test_name = fields.Char(string="Test Name", readonly=True, default="Random Blood Sugar", )
    rbs_value = fields.Float(string="Value", required=True, )
    rbs_normal_value = fields.Text(string="Normal Value", readonly=True, default="(60-160) mg/dl", )

    sc_test_name = fields.Char(string="Test Name", readonly=True, default="S.Creatinine", )
    sc_value = fields.Float(string="Value", required=True, )
    sc_normal_value = fields.Text(string="Normal Value", readonly=True, default="(0.6-1.5) mg/dl", )

    ur_test_name = fields.Char(string="Test Name", readonly=True, default="Urea", )
    ur_value = fields.Float(string="Value", required=True, )
    ur_normal_value = fields.Text(string="Normal Value", readonly=True, default="(15-45) mg/dl", )

    sg_test_name = fields.Char(string="Test Name", readonly=True, default="S.GOT", )
    sg_value = fields.Float(string="Value", required=True, )
    sg_normal_value = fields.Text(string="Normal Value", readonly=True, default="(5-45) U/I", )

    sgp_test_name = fields.Char(string="Test Name", readonly=True, default="S.GPT", )
    sgp_value = fields.Float(string="Value", required=True, )
    sgp_normal_value = fields.Text(string="Normal Value", readonly=True, default="(5-45) U/I", )




