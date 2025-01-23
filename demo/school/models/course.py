from odoo import models, fields

class Course(models.Model):
    _name = 'student.management.course'
    _description = 'Course'

    name = fields.Char(string='Course Name', required=True)
    description = fields.Text(string='Description')
    student_ids = fields.Many2many('student.management.student', string='Students')
    enrollment_ids = fields.One2many('student.management.enrollment', 'course_id', string='Enrollments')
