# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'AgroOffice Management',
    'version': '0.1',
    'author': 'Proyecto Delice',
    'website': 'http://www.proyectodelice.es',
    'category': 'Project Management',
    'sequence': 10,
    'summary': 'Agriculture, Farms, Projects, Tasks',
    'images': [],
    'depends': [
        'purchase',
        'sale',
        'hr',
        'stock',
        'project',
        'project_timesheet', 
        'hr_timesheet_sheet', 
        'sale_analytic_plans',
    ],
    'description': """
Set menu, groups, access and OpenERP for a Farm company processes
=====================================================
    * Custom menus
    * Agro group users
    * Agro model acces rules
    """,
    'data': [
        'security/agro_base_security.xml',
        'security/ir.model.access.csv',
        'agro_menu_view.xml',
        'agro_hr_view.xml',
        'wizard/wizard_crea_parte_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
