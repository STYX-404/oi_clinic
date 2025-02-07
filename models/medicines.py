from odoo import api, fields, models
class Medicines(models.Model):
    _name = 'medicines.data'
    _rec_name = 'med_name'
    _description = 'a model that contain medicines data and information'

    med_name = fields.Char(string="Medicine name", required=True, )
    _sql_constraints = [
        ('med_name_unique', 'unique(med_name)', ' This medicine already exists!')
    ]
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
    med_category_description = fields.Text(string="Description", required=False)
    med_stock = fields.Integer(string="Stock", required=False,)
    med_outgoing = fields.Integer(string="Outgoing", required=False, compute="get_doses" )
    med_code = fields.Char(string="Medicine code", required=False, readonly=True)
    med_notes = fields.Text(string="Additional notes", required=False, )
    med_stock2 = fields.Integer(string="Stock", required=False, compute="update_stock",)
    med_date = fields.Datetime(string="Stock Update Date", default=fields.Datetime.now(),)

    @api.model
    def create(self, values):
        values.update({"med_code": self.env["ir.sequence"].next_by_code("med_code_num")})
        return super(Medicines, self).create(values)

    @api.multi
    def write(self, values):
        return super(Medicines, self).write(values)

    @api.onchange('med_stock')
    def update_date(self):
        for rec in self:
            if rec.med_stock:
                rec.med_date = fields.Datetime.now()

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
            med_date = record.med_date.strftime("%m/%d/%Y, %H:%M:%S")
            for item in get_doses_emp:
                dose = item.med_dose
                dose_2 = item.med_dose_2
                emp_med_name = item.med_ids.med_name
                emp_med_name_2 = item.med_ids_2.med_name
                date = item.em_date.strftime("%m/%d/%Y, %H:%M:%S")
                if date > med_date and medicine_name == emp_med_name:
                    record.med_outgoing += dose
                if date > med_date and medicine_name == emp_med_name_2:
                    record.med_outgoing += dose_2
            for item in get_doses_stu:
                dose = item.med_dose
                dose_2 = item.med_dose_2
                stu_med_name = item.med_ids.med_name
                stu_med_name_2 = item.med_ids_2.med_name
                date = item.stu_date.strftime("%m/%d/%Y, %H:%M:%S")
                if date > med_date and medicine_name == stu_med_name:
                    record.med_outgoing += dose
                if date > med_date and medicine_name == stu_med_name_2:
                    record.med_outgoing += dose_2

    @api.multi
    @api.depends('med_stock' )
    # @api.onchange('med_outgoing')
    def update_stock(self):
        global emp_med_name, dose, stock, medicine_name
        get_doses_emp = self.env["emdailycheckup.data"].search([])
        get_doses_stu = self.env["stdailycheckup.data"].search([])
        for record in self:
            medicine_name = record.med_name
            stock = record.med_stock
            med_date = record.med_date.strftime("%m/%d/%Y, %H:%M:%S")
            for item in get_doses_emp:
                emp_med_name = item.med_ids.med_name
                emp_med_name_2 = item.med_ids_2.med_name
                dose = item.med_dose
                dose_2 = item.med_dose_2
                date = item.em_date.strftime("%m/%d/%Y, %H:%M:%S")
                if date > med_date and medicine_name == emp_med_name:
                    stock -= dose
                    cal = stock
                    record.med_stock2 = cal
                if date > med_date and medicine_name == emp_med_name_2:
                    stock -= dose_2
                    cal = stock
                    record.med_stock2 = cal
            for item in get_doses_stu:
                stu_med_name = item.med_ids.med_name
                stu_med_name_2 = item.med_ids_2.med_name
                dose = item.med_dose
                dose_2 = item.med_dose_2
                date = item.stu_date.strftime("%m/%d/%Y, %H:%M:%S")
                if date > med_date and medicine_name == stu_med_name:
                    stock -= dose
                    cal = stock
                    record.med_stock2 = cal
                if date > med_date and medicine_name == stu_med_name_2:
                    stock -= dose_2
                    cal = stock
                    record.med_stock2 = cal
