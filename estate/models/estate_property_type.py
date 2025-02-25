from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'estate type'

    name = fields.Char('Property type', required=True)
