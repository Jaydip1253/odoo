# models/school_teacher_section.py

from odoo import models, fields

class SchoolTeacherSection(models.Model):
    _name = 'school.teacher.section'
    _description = 'Teacher Section'

    teacher_id = fields.Many2one('school.teacher', string='Teacher', required=True)
    section_id = fields.Many2one('school.section', string='Section', required=True)
    schedule_ids = fields.One2many('school.timetable', 'teacher_section_id', string='Schedule')
