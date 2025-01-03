# models/school_timetable.py

from odoo import models, fields

class SchoolTimetable(models.Model):
    _name = 'school.timetable'
    _description = 'School Timetable'

    teacher_section_id = fields.Many2one('school.teacher.section', string='Teacher Section')
    subject_id = fields.Many2one('school.subject', string='Subject')
    day = fields.Selection([
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
    ], string='Day', required=True)
    time = fields.Float(string='Time (Hours)')
