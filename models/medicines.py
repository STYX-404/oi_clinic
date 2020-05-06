from odoo import api, fields, models
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
    med_stock = fields.Integer(string="Stock", required=False, compute="update_stock", readonly=False)
    med_outgoing = fields.Integer(string="Outgoing", required=False, compute="get_doses" )
    med_code = fields.Char(string="Medicine code", required=False, readonly=True)
    med_notes = fields.Text(string="Additional notes", required=False, )
    med_stock2 = fields.Integer(string="stock2", required=False,)

    @api.model
    def create(self, values):
        values.update({"med_code": self.env["ir.sequence"].next_by_code("med_code_num")})
        return super(Medicines, self).create(values)

    @api.multi
    def write(self, values):
        return super(Medicines, self).write(values)



    #---------------------------------------------------

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

    @api.multi
    @api.depends('med_stock', )
    # @api.onchange('med_outgoing')
    def update_stock(self):

        global emp_med_name, dose, stock, medicine_name
        get_doses_emp = self.env["emdailycheckup.data"].search([])
        get_doses_stu = self.env["stdailycheckup.data"].search([])
        for item in get_doses_emp:
            emp_med_name = item.med_ids.med_name
            dose = item.med_dose
            for record in self:
                stock = record.med_stock
                medicine_name = record.med_name
                if medicine_name == emp_med_name:
                    record.med_stock = stock - dose

        for item in get_doses_stu:
            dose = item.med_dose
            stu_med_name = item.med_ids.med_name
            for record in self:
                stock = record.med_stock
                medicine_name = record.med_name
                if medicine_name == stu_med_name:
                    record.med_stock = stock - dose

