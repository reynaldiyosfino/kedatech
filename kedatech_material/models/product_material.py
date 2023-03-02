from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProductMaterial(models.Model):
    _name = 'product.material'

    code = fields.Char("Material Code", required=True)
    name = fields.Char("Material Name", required=True)
    type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton'),
    ], string='Material Type', copy=False, required=True)
    price_unit = fields.Integer("Material Buy Price", required=True)
    partner_id = fields.Many2one('res.partner', "Related Supplier", required=True)

    @api.constrains('price_unit')
    def _check_price_unit(self):
        """ Function to constraint the price unit """
        if self.price_unit < 100:
            raise ValidationError(_('Material Buy Price cannot be less than 100!'))
