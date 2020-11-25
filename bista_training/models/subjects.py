# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Subjects(models.Model):
    _name = 'bista.subjects'
    _description = 'Subjects Master'

    name = fields.Char('Subject')
    description = fields.Html('Description')
    topics = fields.One2many('bista.topics', 'subject', string='Training Topics')
    trainers = fields.Many2one('bista.trainer', string="Trainer")
