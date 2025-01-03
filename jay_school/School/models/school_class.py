# models/school_class.py

from odoo import models, fields

class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'School Class'

    name = fields.Char(string='Class Name', required=True)
    subject_ids = fields.One2many('school.subject', 'class_id', string='Subjects')
