from odoo import models, fields


class Expenses(models.Model):
    _name = 'expenses'

    description = fields.Text(required=True)
    amount = fields.Float(required=True)
    governorate_id = fields.Many2one('governorate', required=True)
    traffic_department_id = fields.Many2one('traffic.department')
