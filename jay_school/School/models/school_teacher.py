# models/school_teacher.py

from odoo import models, fields

class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    _description = 'School Teacher'

    name = fields.Char(string='Name', required=True)
    employee_id = fields.Char(string='Employee ID')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    subject_ids = fields.One2many('school.subject', 'teacher_id', string='Subjects')
