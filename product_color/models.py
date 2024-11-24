from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    glass_colors = fields.Char(string='Glass Colors')
