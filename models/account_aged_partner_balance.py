# -*- coding: utf-8 -*-

from odoo import models, api, fields, _


class ReportAccountAgedPayable(models.AbstractModel):
    _inherit = 'account.aged.payable'

    partner_code = fields.Char(group_operator='max')

    @api.model
    def _get_sql(self):
        # options = self.env.context['report_options']
        res = super(ReportAccountAgedPayable, self)._get_sql()
        res = res.replace('partner.name AS partner_name',
                          'partner.name AS partner_name , partner.partner_code AS partner_code')
        return res

    @api.model
    def _get_column_details(self, options):
        res = super(ReportAccountAgedPayable, self)._get_column_details(options)
        # res += [
        #     self._field_column('partner_code', name="Partner Code"),
        # ]
        res.append(self._field_column('partner_code'))
        return res
