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

class agro_irrigation_irrigation(osv.osv):
    _name = 'agro.irrigation.irrigation'
    _description = 'Riegos'

    def register_open(self, cr, uid, ids, context=None):
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')

        result = mod_obj.get_object_reference(cr, uid, 'agro_irrigation', 'act_agro_irrigation_register')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        reg_ids = []
        for irrigation in self.browse(cr, uid, ids, context=context):
            reg_ids+= [register.id for register in irrigation.register_ids]
        if not reg_ids:
            result['domain'] = "[('id', 'in', [])]"
        else:
            result['domain'] = "[('id','in',["+','.join(map(str, reg_ids))+"])]"
        return result
    
    _columns={
        'name': fields.char('Nombre', size=50, required = True),
        'propietario_id': fields.many2one('res.partner', 'Propietario', required=True),
        'explotacion_ids': fields.many2many('agro.project.explotacion', 'agro_irrigation_explotacion', 'irrigation_id', 'explotacion_id', 'Explotacion', required = True),
        'toma_id': fields.many2one('agro.irrigation.toma', 'Toma', required = True),
        'bombeo_id': fields.many2one('agro.irrigation.bombeo', 'Bombeo', required = True),
        'fecha_inicio': fields.date('Fecha inicio'),
        'dotacion': fields.float('Dotacion [m3/ha]'),
        'superficie': fields.float('Superficie total'),
        'superficie_riego': fields.float('Superficie a regar'),
        'sistema_riego_id': fields.many2one('agro.irrigation.sistema', 'Sistema de riego'),
        'observaciones': fields.text('Observaciones', size=200),
        'register_ids': fields.one2many('agro.irrigation.register', 'riego_id', 'Registros'),
    }
agro_irrigation_irrigation()

class agro_irrigation_sistema(osv.osv):
    _name = 'agro.irrigation.sistema'
    _description = 'Sistema de riego'

    _columns={
        'name': fields.char('Sistema de riego', size=128, required = True),
    }
agro_irrigation_sistema()

class agro_irrigation_toma(osv.osv):
    _name = 'agro.irrigation.toma'
    _description = 'Toma'
    _rec_name = 'procedencia'

    _columns={
        'procedencia': fields.char('Procedencia', size=128, required = True),
        'coordenada_x': fields.char('Coordenada X[m]', size=8),
        'coordenada_y': fields.char('Coordenada Y[m]', size=8),
        'huso': fields.char('Huso', size=8),
        'proyeccion': fields.char('Sistema de proyeccion', size=8),
        'embalse_id': fields.many2one('agro.irrigation.toma.embalse', 'Embalse'),
        'contador_id': fields.many2one('agro.machine.machine', 'Contador', required = True),
        'precintado': fields.boolean('Contador precintado'),

    }
agro_irrigation_toma()

class agro_irrigation_toma_embalse(osv.osv):
    _name = 'agro.irrigation.toma.embalse'
    _description = 'Embalse de la toma'

    _columns={
        'name': fields.char('Nombre', size=64, required = True),
        'machine_id': fields.many2one('agro.machine.machine', 'Dispositivo', required = True),
        'volumen': fields.float('Volumen embasado [m3/%]'),
        'capacidad': fields.float('Capacidad [m3]'),  
    }
agro_irrigation_toma_embalse()

class agro_irrigation_bombeo(osv.osv):
    _name = 'agro.irrigation.bombeo'
    _description = 'Bombeo'

    _columns={
        'name': fields.char('Nombre', size=64, required = True),
        'machine_id': fields.many2one('agro.machine.machine', 'Dispositivo', required = True),
        'potencia': fields.float('Potencia'),
        'caudal': fields.float('Caudal [L/s]'),
    }
agro_irrigation_bombeo()


class agro_irrigation_register(osv.osv):
    _name = 'agro.irrigation.register'
    _description = 'Registro de Riegos'

    _columns={
        'name': fields.char('Nombre', size=64, required = True),
        'riego_id': fields.many2one('agro.irrigation.irrigation', 'Riego', required=True),
        'tipo_riego_id': fields.many2one('agro.irrigation.register.tipo', 'Tipo de riego'),
        'fecha_inicio': fields.date('Fecha inicio', required = True),
        'fecha_fin': fields.date('Fecha fin'),
        'lectura_inicio': fields.float('Lectura inicial [m3]', required = True),
        'lectura_final': fields.float('Lectura final [m3]'),
        'observaciones': fields.char('Observaciones', size=200),
    }
agro_irrigation_register()

class agro_irrigation_register_tipo(osv.osv):
    _name = 'agro.irrigation.register.tipo'
    _description = 'Tipo de riego'

    _columns={
        'name': fields.char('Tipo de riego', size=128, required = True),
    }
agro_irrigation_register_tipo()

