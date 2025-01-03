# models/school_fee.py

from odoo import models, fields

class SchoolFee(models.Model):
    _name = 'school.fee'
    _description = 'School Fee'

    student_id = fields.Many2one('school.student', string='Student')
    fee_type = fields.Char(string='Fee Type')
    amount = fields.Float(string='Amount')
    due_date = fields.Date(string='Due Date')
    paid_status = fields.Selection([('paid', 'Paid'), ('unpaid', 'Unpaid')], string='Paid Status')
    payment_date = fields.Date(string='Payment Date')
