from odoo import api, fields, models
from .daily_check_up import StudentsFollowUp
from .daily_check_up import EmployeeFollowUp
class Medicines(models.Model):
    _name = 'medicines.data'
    _rec_name = 'med_name'
    _description = 'a model that contain medicines data and information'

    med_name = fields.Char(string="Medicine name", required=True, )
    med_type = fields.Selection(string="Medicine type",
                                selection=
                                [('li', 'Liquid'),
                                 ('dps', 'drops'),
                                 ('cgs', 'Creams & Gels'),
                                 ('inhs', 'Inhalers'),
                                 ('pts', 'patches'),
                                 ('tbls', 'Tablets'),
                                 ('pls', 'Pills'),
                                 ('injs', 'Injections')],
                                required=True, )

    med_category = fields.Selection(string="Medicine category",
                                    selection=
                                    [('atcs', 'Antipyretics'),
                                     ('angs', 'Analgesics'),
                                     ('antcs', 'Antibiotics'),
                                     ('atpcs', 'Antiseptics'),
                                     ('or', 'Other')],
                                    required=True, )
    med_category_description = fields.Text(string="description", required=False)
    med_stock = fields.Integer(string="Stock", required=False, )
    med_outgoing = fields.Integer(string="Outgoing", required=False, compute="get_doses" )
    med_ex_date = fields.Date(string="Expiration date", required=True, )
    med_code = fields.Char(string="Medicine code", required=False, readonly=True)
    med_notes = fields.Text(string="Additional notes", required=False, )

    @api.multi
    @api.depends('med_name', 'med_outgoing',)
    def get_doses(self):

        global emp_med_name, dose, outgoing, medicine_name
        get_doses_emp = self.env["emdailycheckup.data"].search([])
        get_doses_stu = self.env["stdailycheckup.data"].search([])

        for record in self:
            medicine_name = record.med_name
            outgoing = record.med_outgoing
            for item in get_doses_emp:
                dose = item.med_dose
                emp_med_name = item.med_ids.med_name
                if medicine_name == emp_med_name:
                    record.med_outgoing += dose
            for item in get_doses_stu:
                dose = item.med_dose
                stu_med_name = item.med_ids.med_name
                if medicine_name == stu_med_name:
                    record.med_outgoing += dose

