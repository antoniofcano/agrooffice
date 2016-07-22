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


class agro_health_tratamiento_stage(osv.osv):
    _name = 'agro.health.tratamiento.stage'
    _description = 'Tratamiento Stage'
    _order = 'sequence'
    _columns = {
        'name': fields.char('Stage Name', required=True, translate=True),
        'description': fields.text('Description'),
        'sequence': fields.integer('Sequence'),
        'fold': fields.boolean('Folded in Kanban View',
                               help='This stage is folded in the kanban view when'
                               'there are no records in that stage to display.'),
    }

    _defaults = {
        'sequence': 1,
    }
    _order = 'sequence'
agro_health_tratamiento_stage()

class agro_health_tratamiento(osv.osv):
    _name = 'agro.health.tratamiento'
    _description = 'Tratamiento'
    
    _columns={
        'name': fields.char('Nombre', size=50, required = True),
        'campana_id': fields.many2one('project.project', 'Campana', required = True),
        'plaga_ids': fields.many2many('agro.health.plaga', 'agro_tratamiento_plaga', 'tratamiento_id', 'plaga_id', 'Lista de plagas', required = True),
        'explotacion_id': fields.many2one('agro.project.explotacion', 'Explotacion', required = True),
        'tipo_tratamiento_id': fields.many2one('agro.health.tipo.tratamiento', 'Tipo de tratamiento'),
        'fecha_inicio': fields.date('Fecha inicio', required = True),
        'fecha_fin': fields.date('Fecha fin'),
        'tipo_aplicacion_id': fields.many2one('agro.health.tipo.aplicacion', 'Forma de aplicacion'),
        #'machine_id': fields.many2one('agro.machine.machine', 'Maquina aplicacion', ),
        'machine_id': fields.many2one('machinery', 'Maquina', ),
        'dosis_ids': fields.one2many('agro.health.tratamiento.dosis', 'tratamiento_id', 'Dosis de productos'),
        'task_ids': fields.many2many('project.task', 'agro_tratamiento_task', 'tratamiento_id', 'task_id', 'Tareas asociadas', required = True),
        'responsable_id': fields.many2one('res.users', 'Responsable', required = True),
        'observaciones': fields.text('Observaciones'),
        'priority': fields.selection([('0','Low'), ('1','Normal'), ('2','High')], 'Priority', select=True),
        'color': fields.integer('Color Index'),
        'stage_id': fields.many2one('agro.health.tratamiento.stage', 'Stage', track_visibility='onchange', select=True, copy=False),
        'kanban_state': fields.selection([('normal', 'In Progress'),('blocked', 'Blocked'),('done', 'Ready for next stage')], 'Kanban State',
                                         track_visibility='onchange',
                                         help="A tratamiento's kanban state indicates special situations affecting it:\n"
                                              " * Normal is the default situation\n"
                                              " * Blocked indicates something is preventing the progress of this task\n"
                                              " * Ready for next stage indicates the tratamiento is ready to be pulled to the next stage",
                                         required=False, copy=False),
    }

    _order = "fecha_inicio, id"
    _defaults = {
        'kanban_state': 'normal',
    }


agro_health_tratamiento()

class agro_health_tratamiento_dosis(osv.osv):
    _name = 'agro.health.tratamiento.dosis'
    _description = 'Tratamiento dosis'

    _columns={
        'tratamiento_id': fields.many2one('agro.health.tratamiento', 'Tratamiento'),
        'product_id': fields.many2one('agro.health.product', 'Producto'),
        'dosis': fields.float('Dosis'),
        'cantidad': fields.float('Cantidad total'),
        'litros': fields.float('Litros de agua'),
    }
agro_health_tratamiento_dosis()

class agro_health_tipo_tratamiento(osv.osv):
    _name = 'agro.health.tipo.tratamiento'
    _description = 'Tipo de tratamiento'

    _columns = {
        'name': fields.char('Tipo tratamiento', size=128, required = True),
    }

agro_health_tipo_tratamiento()

class agro_health_tipo_aplicacion(osv.osv):
    _name = 'agro.health.tipo.aplicacion'
    _description = 'Forma de aplicacion'
  
    _columns = {
        'name': fields.char('Forma de aplicacion', size=128, required = True),
    }

agro_health_tipo_aplicacion()

