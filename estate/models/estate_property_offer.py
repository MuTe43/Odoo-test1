from datetime import timedelta

from odoo import fields, models, api
from odoo.fields import Datetime


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
    validity = fields.Integer('Validity (days)', default=7)
    date_deadline = fields.Date('Deadline ', compute="_calc_date", inverse='_inverse_calc_date')

    @api.depends("create_date","validity")
    def _calc_date(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + timedelta(days=record.validity)
            else:
                record.date_deadline = Datetime.today() + timedelta(days=record.validity)

    def _inverse_calc_date(self):
        for record in self:
            if record.date_deadline and record.create_date:
                delta = record.date_deadline - record.create_date.date()
                record.validity = delta.days
            else:
                record.validity = (record.date_deadline - fields.Date.today()).days