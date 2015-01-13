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

class agro_machine_machine(osv.osv):
    _name = 'agro.machine.machine'
    _description = 'Maquinaria'

    def repostaje_open(self, cr, uid, ids, context=None):
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')

        result = mod_obj.get_object_reference(cr, uid, 'agro_machine', 'act_agro_machine_repostaje')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        rep_ids = []
        for machine in self.browse(cr, uid, ids, context=context):
            rep_ids+= [repostaje.id for repostaje in machine.repostaje_ids]
        if not rep_ids:
            result['domain'] = "[('id', 'in', [])]"
        else:
            result['domain'] = "[('id','in',["+','.join(map(str, rep_ids))+"])]"
        return result
    
    def service_open(self, cr, uid, ids, context=None):
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')

        result = mod_obj.get_object_reference(cr, uid, 'agro_machine', 'act_agro_machine_service')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        ser_ids = []
        for machine in self.browse(cr, uid, ids, context=context):
            ser_ids+= [service.id for service in machine.service_ids]
        if not ser_ids:
            result['domain'] = "[('id', 'in', [])]"
        else:
            result['domain'] = "[('id','in',["+','.join(map(str, ser_ids))+"])]"
        return result

    _columns={
        'name': fields.char('Maquina', size=128, required = True),
        'marca': fields.many2one('agro.machine.marca', 'Marca'),
        'modelo': fields.char('Modelo', size=128),
        'matricula': fields.char('Matricula', size=10),
        'num_bastidor': fields.char('Bastidor', size=128, required = True),
        'tipo_maquina_id': fields.many2one('agro.machine.tipo', 'Tipo de maquina'),
        'titular_id': fields.many2one('res.partner', 'Titular'), 
        'explotacion_id': fields.many2one('agro.project.explotacion', 'Explotacion asociada'),
        'service_ids': fields.one2many('agro.machine.service', 'machine_id', 'Servicio y mantenimiento'),
        'repostaje_ids': fields.one2many('agro.machine.repostaje', 'machine_id', 'Repostaje'),
        'order_id': fields.many2one('purchase.order', 'Orden de compra'),
        'garantia': fields.date('Fecha fin de garantia', ),
        'machine_ids': fields.many2many(
            'agro.machine.machine',
            'agro_machine_machine_kit',
            'machine_kit_id',
            'machine_id',
            'Kit'),
    }
agro_machine_machine()

class agro_machine_marca(osv.osv):
    _name = 'agro.machine.marca'
    _description = 'Marca'

    _columns={
        'name': fields.char('Marca', size=128, required = True),
    }
agro_machine_marca()

class agro_machine_tipo(osv.osv):
    _name = 'agro.machine.tipo'
    _description = 'Tipo de maquina'

    _columns={
        'name': fields.char('Tipo de maquina', size=128, required = True),
    }
agro_machine_tipo()

class agro_machine_service(osv.osv):
    _name = 'agro.machine.service'
    _description = 'Mantenimiento y Averias'
    _rec_name = 'machine_id'

    _columns={
        'machine_id': fields.many2one('agro.machine.machine', 'Maquina', required = True),
        'descripcion': fields.char('Descripcion', size=128),
        'fecha': fields.date('Fecha', required = True),
        'lectura': fields.float('Kms/Horas/...'),
        'coste': fields.float('Coste', required = True),
        'service_tipo_id': fields.many2one('agro.machine.service.tipo', 'Tipo de mantenimiento', required = True),
        'explotacion_id': fields.many2one('agro.project.explotacion', 'Explotacion', required = True),
        'campana_id': fields.many2one('project.project', 'Campana', required = True),
        'task_id': fields.many2one('project.task', 'Tarea asociada', required = True),
        'responsable_id': fields.many2one('res.users', 'Responsable', required = True),
        'observaciones': fields.text('Observaciones'),
        'order_id': fields.many2one('purchase.order', 'Orden de compra'),
    }
agro_machine_service()

class agro_machine_service_tipo(osv.osv):
    _name = 'agro.machine.service.tipo'
    _description = 'Tipo de mantenimiento'

    _columns={
        'name': fields.char('Tipo de mantenimiento', size=128, required = True),
    }
agro_machine_service_tipo()

class agro_machine_repostaje(osv.osv):
    _name = 'agro.machine.repostaje'
    _description = 'Repostaje'
    _rec_name = 'machine_id'

    _columns={
        'machine_id': fields.many2one('agro.machine.machine', 'Maquina', required = True),
        'fecha': fields.date('Fecha', required = True),
        'lectura': fields.float('Kms/Horas/...'),
        'coste': fields.float('Coste', required = True),
        'explotacion_id': fields.many2one('agro.project.explotacion', 'Explotacion', required = True),
        'campana_id': fields.many2one('project.project', 'Campana', required = True),
        'task_id': fields.many2one('project.task', 'Tarea asociada', required = True),
        'tipo_labor_id': fields.related(
            'task_id',
            'tipo_labor_id',
            'name',
            type="char",
            relation="project.task",
            string="Tipo de Labor",
            store=True),
        'tipo_repostaje_id': fields.many2one('agro.machine.repostaje.tipo', 'Tipo de repostaje'),
        'responsable_id': fields.many2one('res.users', 'Responsable', required = True),
        'order_id': fields.many2one('purchase.order', 'Orden de compra'),
    }
agro_machine_repostaje()

class agro_machine_repostaje_tipo(osv.osv):
    _name = 'agro.machine.repostaje.tipo'
    _description = 'Tipo de repostaje'

    _columns={
        'name': fields.char('Tipo de repostaje', size=128, required = True),
    }
agro_machine_repostaje_tipo()

