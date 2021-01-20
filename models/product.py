# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class ProductProduct(models.Model):
    _inherit = "product.product"

    # @api.model
    # def _name_search(self, name, args, limit=None):
    #     # override only search
    #     # if self._context.get('search_by_pricelist_id', True):
    #     if name:
    #         args = args if args else []
    #         args.extend(['pricelist_id', 'ilike', name])
    #         name = ''
    #     return super(ProductProduct, self)._name_search(name=name, args=args, operator=operator, limit=limit)

    # @api.model
    # def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
    #     context = self._context or {}
    #     # if context.get('check_pricelist', True) and context.get('pricelist'):
    #         # product_id = self.env['res.partner'].search([('id', '=', context.get('partner_id'))])
    #     if context.get('check_pricelist', True):
    #         pdt_tmpl_ids = self.env['product.pricelist.item'].search(
    #             [('pricelist_id', '=', context.get('pricelist'))]).mapped('product_tmpl_id').ids
    #         print(pdt_tmpl_ids)
    #         args += [('product_tmpl_id', 'in', pdt_tmpl_ids)]
    #     res = super(ProductProduct, self)._search(args, offset=offset, limit=limit, order=order, count=count,
    #                                               access_rights_uid=access_rights_uid)
    #     return res

    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        context = self._context or {}
        # Display product based on pricelist field in header
        if context.get('filter_basedon_pricelist') and context.get('pricelist_id'):
            pdt_tmpl_ids = self.env['product.pricelist.item'].search([('pricelist_id', '=', context.get('pricelist_id'))]).mapped('product_tmpl_id').ids
            args += [('product_tmpl_id', 'in', pdt_tmpl_ids)]

        # Display product based on product category field in header
        if context.get('filter_basedon_product_category') and context.get('category_id'):
            product_cat_ids = self.env['product.template'].search([('categ_id', '=', context.get('category_id'))]).mapped('categ_id').ids
            print("Test", product_cat_ids)
            args += [('categ_id', 'in', product_cat_ids)]

        # domain = [('category_id')]
        # print("!!", domain)
        # if domain:
        #     product_cat_ids = self.env['product.template'].search([('categ_id', '=', 'category_id')]).mapped('categ_id').ids
        #     print("Test", product_cat_ids)
        #     args += [('categ_id', 'in', product_cat_ids)]

        return super(ProductProduct, self)._search(args, offset=offset, limit=limit, order=order, count=count,
                                                  access_rights_uid=access_rights_uid)

    # @api.model
    # def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
    #     if not args:
    #         args = []
    #     if name:
    #         product_ids = []
    #         if not product_ids and self._context.get('partner_id'):
    #             pdt_template_ids = self.env['product.pricelist.item']._search([
    #                 ('name', '=', self._context.get('partner_id'))], access_rights_uid=name_get_uid)
    #             if pdt_template_ids:
    #                 product_ids = self._search([('product_tmpl_id.name', 'in', item_ids)], limit=limit,
    #                                            access_rights_uid=name_get_uid)
    #     else:
    #         product_ids = self._search(args, limit=limit, access_rights_uid=name_get_uid)
    #     return product_ids

    # @api.model
    # def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
    #     if self._context.get('check_pricelist', False):
    #         return super(ProductProduct, self)._search(args, offset=offset, limit=limit, order=order, count=count, access_rights_uid=access_rights_uid)
    #     product_list = []
    #     pricelist = self.env['product.pricelist'].browse(self._context.get('pricelist'))
    #     if pricelist:
    #         for record in pricelist.item_ids:
    #             if record.applied_on == '0_product_variant':
    #                 product_list.append(record.product_id.id)
    #         # args += [('product_tmpl_id', 'in', pricelist)]
    #     if product_list:
    #         self = self.browse(product_list)
    #     result = super(ProductProduct, self)._search(args, offset=offset, limit=limit, order=order, count=count, access_rights_uid=access_rights_uid)
    #     return result

    # @api.model
    # def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
    #     context = self._context or {}
    #     if context.get('product_id'):
    #         product = self.env['product.product'].browse(context.get('product_id'))
    #         if product:
    #             args += [('product_id', '=', product.pricelist.item_ids)]
    #     res = super(ProductProduct, self)._search(args, offset=offset, limit=limit, order=order, count=count,
    #                                               access_rights_uid=access_rights_uid)
    #     return res

    # @api.model
    # def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
    #     if self._context.get('product_id'):
    #         args.append((('pricelist_id.item_ids.product_tmpl_id', self._context['product_id'])))
    #     return super(ProductProduct, self)._search(args, offset=offset, limit=limit, order=order, count=count,
    #                                                access_rights_uid=access_rights_uid)

    # @api.onchange('pricelist_id')
    # def onchange_field_pricelist(self):
    #     if self.pricelist_id:
    #         # filter products by seller
    #         product_ids = self.pricelist_id.item_ids.product_tmpl_id
    #         print("Test", product_ids)
    #         res = {'domain': {'order_line.product_id': [('id', 'in', product_ids)]}}
    #         return res
    #     else:
    #         # filter all products -> remove domain
    #         return {'domain': {'product_id': []}}

    # def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
    #     context = self._context or {}
    #     if context.get('check_pricelist', True):
    #         # filter products by pricelist_id
    #         # product_ids = self.pricelist_id.item_ids.product_tmpl_id
    #         product_ids = self.env['product.pricelist']._search([('id', '=', context.get('pricelist_id'))])
    #         print("Test", product_ids)
    #         # res = {'domain': {'order_line.product_id': [('id', 'in', product_ids)]}}
    #         # print("Test2", res)
    #         return super(ProductProduct, self)._search(args, offset=offset, limit=limit, order=order, count=count,
    #                                                    access_rights_uid=access_rights_uid)
