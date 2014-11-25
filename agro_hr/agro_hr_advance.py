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

class agro_hr_advance(osv.osv):    
    _name = 'agro.hr.advance'
    _description = 'Adelantos de nomina'
    
    _columns={
            'empleado_id': fields.many2one('hr.employee', 'Empleado', required = True),
            'campana_id': fields.many2one('project.project', 'Campana', required = True),
            'fecha': fields.date('Fecha', required= True),
            'cantidad': fields.float('Cantidad', required= True),
    }

agro_hr_advance()
