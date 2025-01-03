# models/school_attendance.py

from odoo import models, fields

class SchoolAttendance(models.Model):
    _name = 'school.attendance'
    _description = 'School Attendance'

    student_id = fields.Many2one('school.student', string='Student')
    teacher_id = fields.Many2one('school.teacher', string='Teacher')
    date = fields.Date(string='Date')
    status = fields.Selection([('present', 'Present'), ('absent', 'Absent'), ('late', 'Late')], string='Status')
    remarks = fields.Text(string='Remarks')
