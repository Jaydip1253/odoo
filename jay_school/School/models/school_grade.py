# models/school_grade.py

from odoo import models, fields

class SchoolGrade(models.Model):
    _name = 'school.grade'
    _description = 'School Grade'

    student_id = fields.Many2one('school.student', string='Student')
    subject_id = fields.Many2one('school.subject', string='Subject')
    marks = fields.Float(string='Marks')
    grade = fields.Selection([('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], string='Grade')
