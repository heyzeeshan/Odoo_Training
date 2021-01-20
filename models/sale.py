# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # @api.onchange('pricelist_id')
    # def _show_pricelist_product(self):
    #     # loop to avoid singleton error
    #     for rec in self:
    #         # add new fields and remove existing one
    #         lines = [(5, 0, 0)]
    #         # loop in batch_ids with our data
    #         for line in self.pricelist_id.item_ids:
    #             lines.append((0, 0, {'product_id': line.id, 'name': line.name}))
    #         # print('lines', lines)
    #         rec.order_line = lines

    # @api.model
    # def _name_search(self, name='', args=None, operator='ilike', limit=100):
    #     if self._context.get('search_by_pricelist_id', True):
    #         if name:
    #             args = args if args else []
    #             args.extend(['pricelist_id', 'ilike', name])
    #             name = ''
    #     return super(SaleOrder, self).name_search(name=name, args=args, operator=operator, limit=limit)

    product_category = fields.Many2one('product.category', string="Product Category")

