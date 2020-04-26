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
    med_stock = fields.Integer(string="In stock", required=True, )
    med_ex_date = fields.Date(string="Expiration date", required=True, )
    med_code = fields.Char(string="Medicine code", required=False, readonly=True)
    med_notes = fields.Text(string="Additional notes", required=False, )


    @api.model
    def create(self, values):
        values.update({"med_code": self.env["ir.sequence"].next_by_code("med_code_num")})
        return super(Medicines, self).create(values)

    @api.multi
    def write(self, values):
        return super(Medicines, self).write(values)