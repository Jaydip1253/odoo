from odoo import models, fields

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    name = fields.Char('Student Name', required=True)
    roll_no = fields.Char('Roll Number', required=True)
    dob = fields.Date('Date of Birth')
    address = fields.Text('Address')
    parent_contact = fields.Char('Parent/Guardian Contact')
    class_id = fields.Many2one('school.class', string='Class')
    section_id = fields.Many2one('school.section', string='Section')


class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'School Class'

    name = fields.Char('Class Name', required=True)


class SchoolSection(models.Model):
    _name = 'school.section'
    _description = 'School Section'

    name = fields.Char('Section Name', required=True)
