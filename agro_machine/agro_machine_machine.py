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

class agro_machine_machine(osv.osv):
    _name = 'agro.machine.machine'
    _description = 'Maquinaria'
    
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
        'observaciones': fields.char('Observaciones', size=200),
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
