
{
    'name': 'Student Management System',
    "summary": 'School',
    "author": 'Jaydip Dhavale',
    'version': '1.0',
    'category': '',
    'sequence': -100,
    'depends': ['base'],
    'description': """
            Student Management System
       """,
    'data': ['security/security.xml',
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/course_views.xml',
        'views/enrollment_views.xml',
        'views/menu.xml',
        'views/attendance.xml'],
    'demo': [],
    'images': [],
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'application': True,
    'license': 'LGPL-3',
}
