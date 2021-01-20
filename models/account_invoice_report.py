# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    partner_code = fields.Char(string='Partner Code')

    @api.model
    def _select(self):
        res = super(AccountInvoiceReport, self)._select()
        # print('Hello', res)
        res = res.replace('line.journal_id',
                          'line.journal_id, partner.partner_code')
        # print('Bye', res)
        return res
