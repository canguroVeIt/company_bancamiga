from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    bank_token_bancamiga = fields.Char(string='Token Bancamiga', help='Token único asociado al banco de esta sede.')
    company_name = fields.Char(string='Razon Social', help='Nombre de la empresa legalmente')
    rif = fields.Char(string='R.I.F', help='RIF')