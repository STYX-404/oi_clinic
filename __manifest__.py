# -*- coding: utf-8 -*-
{
    'name': "oi_clinic",

    'summary': """
        A health care system for the obour institutes clinic.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/students_view.xml',
        'sequences/students_code.xml',
        'views/employees_view.xml',
        'sequences/employees_code.xml',
        'views/docs_and_nurses_views.xml',
        'sequences/docsAndNurses_code.xml',
        'views/laboratory_view.xml',
        'views/daily_check_up_view.xml',
        'views/health_report_view.xml',
        'views/medicines_views.xml',
        'sequences/med_code.xml',
        'report/st_health_reports.xml',
        'report/st_health_report.xml',
        'sequences/laboratory_code.xml',
        'report/students_report.xml',
        'report/stu_reports.xml',
        'report/lab_report.xml',
        'report/laboratory_report.xml',
        'report/students_dailycheckup_reports.xml',
        'report/student_dailycheckup_report.xml',
        'report/employees_dailycheckup_reports.xml',
        'report/employee_dailycheckup_report.xml',
        'report/docandnur_reports.xml',
        'report/doctorandnurse_report.xml',
        'report/em_health_reports.xml',
        'report/em_health_report.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}