# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Trainer(models.Model):
    _name = 'bista.trainer'
    _description = 'Trainer Master'

    id = fields.Integer('ID')
    # compute for creating api depend for concat
    name = fields.Char(compute='comp_name', store=True)
    first_name = fields.Char('First Name')
    last_name = fields.Char('Last Name')
    profile = fields.Binary('Profile Image', attachment=True, store=True)

    # api depend for firstname and last name concatinate

    @api.depends('first_name', 'last_name')
    def comp_name(self):
        self.name = (self.first_name or '') + ' ' + (self.last_name or '')
