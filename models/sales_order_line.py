from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    serial_number = fields.Char(string="Serial Number", readonly=True)
    product_image = fields.Binary(
        string="Product Image",
        compute="_compute_product_image",
        store=True
    )

    @api.depends('product_id', 'product_image')
    def _compute_product_image(self):
        """Use uploaded product image; otherwise, use product master image."""
        for line in self:
            line.product_image = line.product_image or line.product_id.image_1920

    @api.model
    def create(self, vals):
        """Automatically assign a serial number to each new order line."""
        order = self.env['sale.order'].browse(vals.get('order_id', False))
        if order:
            last_serial = max(order.order_line.mapped('serial_number') or [0])
            vals['serial_number'] = str(int(last_serial) + 1)  # Increment last serial number
        return super(SaleOrderLine, self).create(vals)
