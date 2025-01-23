from odoo import models, fields

class Attendance(models.Model):
    _name = 'student.management.attendance'
    _description = 'Attendance'

    course_id = fields.Many2one('student.management.course', string='Course', required=True)
    student_id = fields.Many2one('student.management.student', string='Student', required=True)
    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    status = fields.Selection([('present', 'Present'), ('absent', 'Absent')], string='Status', required=True)
