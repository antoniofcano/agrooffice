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
from openerp.osv import osv, fields
from openerp.tools.translate import _
from openerp import tools
import time

class wizard_crea_parte(osv.osv_memory):    
    _name = 'wizard.crea.parte'
    _description = 'Para crear partes en lote'
    
    _columns={
            'campana_id': fields.many2one('project.project', 'Campana', required = True),
            'tarea_id': fields.many2one('project.task', 'Tarea', required = True),
            'resumen': fields.char('Resumen del trabajo', size=128, required = True),
            'horas': fields.float('Tiempo dedicado', required = True),
            'fecha': fields.datetime('Fecha', required= True),
            'employee_ids':fields.many2many('hr.employee','rel_partes_trabajadores','parte_id','employee_id', required = True),
              }
    
    _defaults={
            'fecha': lambda *a: time.strftime('%Y-%m-%d'),
            'horas': 7
    }

    def crea_partes(self, cr, uid, ids, context):
        #########################################################################
        # OBJETOS
        #########################################################################
        empleados_obj = self.pool.get('hr.employee')

        wizard_data = self.browse(cr, uid, ids[0], context)
        employe_list = self.browse(cr, uid, ids[0], context).employee_ids
        for emp in employe_list:
            empleado = empleados_obj.browse(cr, uid, emp.id, context)
            val = {
                   'user_id': empleado.user_id.id, 
                   'date': wizard_data.fecha,
                   'name': wizard_data.resumen, 
                   'task_id': wizard_data.tarea_id.id, 
                   'hours': wizard_data.horas,
                   }
	    parte = self.pool.get('project.task.work').create(cr, uid, val)
        return {'type': 'ir.actions.act_window_close'}
    
    def cerrar(self, cr, uid, ids, context): 
        return {'type': 'ir.actions.act_window_close'}        

wizard_crea_parte()
