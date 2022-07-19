from datetime import datetime
from odoo import models, fields, api, _

car_type_list = [
    ('mini_bus', 'ميني باص'),
    ('bus', 'باص'),
    ('micro_bus', 'ميكروباص'),
    ('car', 'ملاكي')]


class CertificateType(models.Model):
    _name = 'certificate.type'
    _translate = True

    name = fields.Char(required=True, translate=True)
    car_type = fields.Selection(car_type_list,
                                default='car', required=True)


class Certificate(models.Model):
    _name = 'certificate'
    _rec_name = 'customer'
    _translate = True

    customer = fields.Many2one('res.partner', required=True)
    motor_number = fields.Char(required=True)
    chassis_number = fields.Char(required=True)
    car_model = fields.Selection([
        (str(num), str(num)) for num in range(datetime.now().year + 1,
                                              datetime.now().year - 70, -1)
    ], required=True)
    brand = fields.Many2one('car.brand')
    other_brand = fields.Boolean(string="ماركات أخري")
    other_brand_text = fields.Char(string="ماركة")
    certificate_type = fields.Many2one('certificate.type', required=True)
    car_type = fields.Selection(car_type_list, required=True, string="نوع السيارة")
    traffic_department_id = fields.Many2one('traffic.department', required=True)
    price = fields.Integer(required=True, string="السعر")
    reference_no = fields.Char(required=True, readonly=True, string="سيريال")
    number_of_prints = fields.Integer()
    allowed_to_print = fields.Boolean(default=True)

    @api.model
    def create(self, vals):
        vals['reference_no'] = self.env['ir.sequence'].next_by_code('certificate')
        return super().create(vals)

    def re_allow_certificate_printing(self):
        self.allowed_to_print = True


class TrafficDepartment(models.Model):
    _name = 'traffic.department'
    _translate = True

    name = fields.Char(required=True)
    governorate_id = fields.Many2one('governorate', required=True)


class Governorate(models.Model):
    _name = 'governorate'
    _translate = True

    name = fields.Char()


class CarBrand(models.Model):
    _name = 'car.brand'

    name = fields.Char()
