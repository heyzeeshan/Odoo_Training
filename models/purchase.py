# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    quote_ref = fields.Char('Vendor Quote Ref')

    def _prepare_invoice(self):
        # Passing quote_ref to vendor bill bill_ref
        invoice_vals = super(PurchaseOrder,self)._prepare_invoice()
        invoice_vals['bill_ref'] = self.quote_ref
        return invoice_vals
