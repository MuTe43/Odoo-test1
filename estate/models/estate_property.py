from datetime import timedelta

from odoo import fields, models
from odoo.fields import Datetime


class EstateProperty(models.Model):
    _name = "estate.property.test"
    _description = "estate desc"


    name = fields.Char('Name', required=True, translate=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date('Available From',default=Datetime.today()+timedelta(30*3),copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer('Living Area (sqm)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Type',
        selection = [('NORTH', 'North'), ('south','South'),('east','East'),('west','West')],
        help = 'Type is used to separate lEADS AND oPPORTUNITIES'
    )
    active= fields.Boolean(default=True)
    state = fields.Selection(default="NEW",
        string='Type',
        selection=[('NEW', 'New'), ('OFFER RECEIVED', 'offer received'), ('OFFER ACCEPTED', 'offer accepted'), ('SOLD', 'sold'), ('CANCELLED', 'cancelled')],
        help='Type is used to separate lEADS AND oPPORTUNITIES'
    )