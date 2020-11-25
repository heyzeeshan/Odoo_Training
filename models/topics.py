# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Topics(models.Model):
    _name = 'bista.topics'
    _description = 'Topics Master'

    name = fields.Char('Name')
    subject = fields.Many2one('bista.subjects', string='Training Subjects')
