# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Delice (<http://proyectodelice.es>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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
from osv import osv, fields
from tools.translate import _
import time
import datetime

class agro_hr_edu(osv.osv):    
    _name = 'agro.hr.edu'
    _description = 'Registra estudios y certificados'
    
    _columns={
            'name': fields.char('Curso', size=200, required = True),
            'empleado_id': fields.many2one('hr.employee', 'Empleado', required = True),
            'fecha_curso': fields.date('Fecha del curso', required= True),
            'carnet': fields.boolean('Dispone del carnet', required= True),
            'fecha_renovacion': fields.date('Fecha renovacion',),
    }

agro_hr_edu()
