# models/school_student.py

from odoo import models, fields

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    name = fields.Char(string='Name', required=True)
    roll_no = fields.Char(string='Roll Number')
    dob = fields.Date(string='Date of Birth')
    address = fields.Text(string='Address')
    parent_contact = fields.Char(string='Parent Contact')
    class_id = fields.Many2one('school.class', string='Class')
    section_id = fields.Many2one('school.section', string='Section')
    guardian_name = fields.Char(string='Guardian Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    admission_date = fields.Date(string='Admission Date')
    student_image = fields.Binary(string='Student Image')
    active = fields.Boolean(string='Active', default=True)
