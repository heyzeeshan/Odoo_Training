# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Location(models.Model):
    _name = 'bista.location'
    _description = 'Location Master'

    name = fields.Char('Location Name', store=True)
    street = fields.Char('Street 1')
    street2 = fields.Char('Street 2')
    city = fields.Char('City')
    country_id = fields.Many2one('res.country', string='Country')
    state_id = fields.Many2one('res.country.state', string='State')
