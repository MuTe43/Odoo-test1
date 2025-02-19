from odoo import fields, models, api


class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'estate tag'

    name = fields.Char(required=True)
