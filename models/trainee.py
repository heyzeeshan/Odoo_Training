# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import datetime
from odoo.exceptions import ValidationError


class Trainee(models.Model):
    _name = 'bista.trainee'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Trainee Master'

    id = fields.Integer('ID')
    profile = fields.Binary('ProfileImage', attachment=True, store=True)
    trainee_id = fields.Char(string='Trainee ID',
                             default=lambda self: self.env['ir.sequence'].next_by_code('trainee.id'))
    # compute for creating api depend for concat
    name = fields.Char(compute='comp_name', store=True)
    first_name = fields.Char('First Name', tracking=True)
    last_name = fields.Char('Last Name')
    email = fields.Char('Email')
    # Many2one for relation with other class of many to one(i.e many trainee two one batch)
    trainee_batch = fields.Many2one('bista_training.bista_training', string="Batch", help="Pick up your batch")
    emp_code = fields.Char('EMP Code')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='male')
    dob = fields.Date('DOB')
    doj = fields.Date('DOJ')
    location = fields.Many2one('bista.location', string='Location')
    designation = fields.Many2one('bista.designation', string='Designation')
    status = fields.Selection(
        [('new', 'New'),
         ('training', 'Training'),
         ('rejected', 'Rejected'),
         ('employed', 'Employed')], string='Status', default='new')
    employee_id = fields.Many2one('hr.employee', string="Employee Details")
    performance = fields.Selection(
        [('0', 'Fail'),
         ('1', 'Poor'),
         ('2', 'Need Improvement'),
         ('3', 'Good'),
         ('4,', 'Very Good'),
         ('5', 'Excellent')
         ], tracking=True
    )

    # dob future date not allowed logic
    # @api.constrains('dob')
    # def _check_dob_date(self):
    #     if self.dob > datetime.date.today():
    #         raise ValidationError(_('Please enter correct dob'))

    # api depend for firstname and last name concatination
    @api.depends('first_name', 'last_name')
    def comp_name(self):
        self.name = (self.first_name or '') + ' ' + (self.last_name or '')

    # sql constraint for unique id
    _sql_constraints = [
        ('trainee_id_unique', 'unique(trainee_id)', ' Please enter Unique id.'),
        ('emp_code', 'unique(emp_code)', ' Please enter Unique EMP_code.'),
    ]

    # employement status change and adding contact in hr.employee
    def action_employment(self):
        # actions
        for rec in self:
            rec.status = 'employed'
            employee_data = {
                'name': rec.name,
                'work_email': rec.email,
                'image_1920': rec.profile,
            }
            employee_record = self.env['hr.employee'].create(employee_data)
            rec.employee_id = employee_record.id

        return True

    # onchange method for dob future date not allowed
    # onchange is to show the validation on time of editing
    # instead of using constraints which show validation error while saving
    @api.onchange('dob')
    def _check_dob_date(self):
        if self.dob and self.dob > datetime.date.today():
            raise ValidationError(_('Please enter correct dob'))
