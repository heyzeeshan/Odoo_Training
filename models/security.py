# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import Warning


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def unlink(self):
        if not self.env.user.has_group('security_groups.delete_product_group'):
            raise Warning(_("You are not allowed to Delete the record"))
        return super().unlink()
