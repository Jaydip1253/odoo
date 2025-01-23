from odoo import models, fields

class Enrollment(models.Model):
    _name = 'student.management.enrollment'
    _description = 'Enrollment'

    student_id = fields.Many2one('student.management.student', string='Student', required=True)
    course_id = fields.Many2one('student.management.course', string='Course', required=True)
    date_enrolled = fields.Date(string='Date Enrolled', default=fields.Date.today)
