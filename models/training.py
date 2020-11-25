# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BistaTraining(models.Model):
    _name = 'bista_training.bista_training'
    _description = 'Bista Training'

    name = fields.Char('Name')
    intern = fields.Char('No of Interns')
    date = fields.Date('Date of Exam')
    trainee_ids = fields.One2many('bista.trainee', 'trainee_batch', string="Trainee")






