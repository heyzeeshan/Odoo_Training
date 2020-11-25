# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Designation(models.Model):
    _name = 'bista.designation'
    _description = 'Designation Master'

    name = fields.Char('Name')
