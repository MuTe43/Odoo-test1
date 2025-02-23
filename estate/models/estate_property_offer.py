from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'estate.property.offer'
    _description = 'offers'

    price = fields.Float()
    status = fields.Selection(
        copy=False,
        selection = [('ACCEPTED', 'accepted'),('REFUSED','refused')]
    )
    partner_id = fields.Many2one('res.partner', required=True)
    property_id= fields.Many2one('estate.property.test', required=True)
