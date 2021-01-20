# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.exceptions import Warning


class Partner(models.Model):
    _inherit = 'res.partner'

    partner_code = fields.Char('Partner Code',
                               default=lambda self: self.env['ir.sequence'].next_by_code('partner.code'))

    _sql_constraints = [
        ('partner_code_unique', 'unique(partner_code)', ' Please enter Partner Code.'),
    ]

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100):
        if self._context.get('search_by_partner_code', True):
            if name:
                args = args if args else []
                args.extend(['|', ['name', 'ilike', name], ['partner_code', 'ilike', name]])
                name = ''
        return super(Partner, self)._name_search(name=name, args=args, operator=operator, limit=limit)

    def write(self, values):
        if not self.env.user.has_group('security_groups.edit_partner_group'):
            raise Warning(_("You are not allowed to Edit the record"))

        return super(Partner, self).write(values)
