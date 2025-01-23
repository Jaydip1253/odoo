from odoo import models, fields

class Student(models.Model):
    _name = 'student.management.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    email = fields.Char(string='Email')
    gender = fields.Selection([('male', 'Male'),('female','Female')], string='Gender')
    course_ids = fields.Many2many('student.management.course', string='Courses')