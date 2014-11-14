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
    'name': 'AgroOffice Project Management',
    'version': '0.1',
    'author': 'Proyecto Delice',
    'website': 'http://www.proyectodelice.es',
    'category': 'Project Management',
    'sequence': 10,
    'summary': 'Agriculture, Farms, Projects, Tasks',
    'images': [],
    'depends': [
        'agro_base',
    ],
    'description': """
Vertical Project management for a Farm company
==============================================
    * Agro project modules
      * Harvest
      * Applications
    """,
    'data': [
        'security/ir.model.access.csv',
        'agro_project_pesada_view.xml',
        'agro_project_variedad_view.xml',
        'agro_project_cultivo_view.xml',
        'agro_project_explotacion_view.xml',
        'agro_project_project_view.xml',
        'agro_project_task_view.xml',
        'agro_res_parner_view.xml',
        'agro_project_parcela_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
