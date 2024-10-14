from odoo import api, fields, models, tools, _, SUPERUSER_ID


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # update discount value in backend and checkout
    def _convert_to_tax_base_line_dict(self, **kwargs):
        self.ensure_one()
        return self.env['account.tax']._convert_to_tax_base_line_dict(
            self,
            partner=self.order_id.partner_id,
            currency=self.order_id.currency_id,
            product=self.product_id,
            taxes=self.tax_id,
            price_unit=self.product_id.product_tmpl_id.get_discount_value() if self.product_id.product_tmpl_id.discount_percentage > 0 else self.price_unit,
            quantity=self.product_uom_qty,
            discount=self.discount,
            price_subtotal=self.product_id.product_tmpl_id.get_discount_value() if self.product_id.product_tmpl_id.discount_percentage > 0 else self.price_subtotal,
            **kwargs,
        )