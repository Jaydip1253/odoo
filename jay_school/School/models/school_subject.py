# models/school_subject.py

from odoo import models, fields

class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'School Subject'

    name = fields.Char(string='Subject Name', required=True)
    class_id = fields.Many2one('school.class', string='Class')
    teacher_id = fields.Many2one('school.teacher', string='Teacher')
