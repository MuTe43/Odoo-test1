from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property.test"
    _description = "estate desc"


    name = fields.Char('Plan Name', required=True, translate=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Type',
        selection = [('NORTH', 'North'), ('south','South'),('east','East'),('west','West')],
        help = 'Type is used to separate lEADS AND oPPORTUNITIES'
    )