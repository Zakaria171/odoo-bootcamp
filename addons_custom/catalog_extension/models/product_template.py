from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    badge_label = fields.Char(string = "Badge")
    warranty_months = fields.Integer(string = "Warranty (Months)")
    product_origin = fields.Selection(
        selection=[
        ("morocco", "Morocco"),
        ("france", "France"),
        ("china", "China"),
        ],
        string = "Origin")
    is_promo_active = fields.Boolean(string = "Promo Active")