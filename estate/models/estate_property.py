from datetime import timedelta

from odoo import fields, models
from odoo.fields import Datetime


class EstateProperty(models.Model):
    _name = "estate.property.test"
    _description = "estate desc"


    name = fields.Char('Name', required=True)
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
        string='Orientation',
        selection = [('NORTH', 'North'), ('south','South'),('east','East'),('west','West')],
        help = 'Garden Orientation'
    )
    active= fields.Boolean(default=True)
    state = fields.Selection(default="NEW",
        string='State',
        selection=[('NEW', 'New'), ('OFFER RECEIVED', 'offer received'), ('OFFER ACCEPTED', 'offer accepted'), ('SOLD', 'sold'), ('CANCELLED', 'cancelled')],
        help='The availability state'
    )

    def _current_user(self):
            return self.env.user

    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    buyer = fields.Many2one("res.partner", string="Buyer")
    salesperson = fields.Many2one("res.users", string="Salesman", default=lambda self : self._current_user())
    tag_ids = fields.Many2many("estate.property.tag")
