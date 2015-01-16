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

class agro_project_weather_station(osv.osv):
    _name = 'agro.project.weather.station'
    _description = 'El Tiempo'

    def historico_open(self, cr, uid, ids, context=None):
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')

        result = mod_obj.get_object_reference(cr, uid, 'agro_project', 'act_agro_project_weather')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]

        data_ids = []
        for station in self.browse(cr, uid, ids, context=context):
            data_ids += [data.id for data in station.data_ids]

        if not data_ids:
            result['domain'] = "[('id', 'in', [])]"
        else:
            result['domain'] = "[('id','in',["+','.join(map(str, data_ids))+"])]"
        return result

    _columns={
            'name': fields.char('Nombre', size=60),
            'provincia': fields.char('Provincia', size=60),
            'cod_estacion': fields.integer('Cod. Estacion'),
            'coord_utm_x': fields.float('Coordenada X'),
            'coord_utm_y': fields.float('Coordenada Y'),
            'web': fields.char('Web', size=400),
            'observaciones': fields.text('Observaciones'),
            'data_ids': fields.one2many('agro.project.weather', 'station', 'Datos Historicos'),
    }
agro_project_weather_station()

class agro_project_weather(osv.osv):
    _name = 'agro.project.weather'
    _description = 'El Tiempo'

    _columns={
            'station': fields.many2one('agro.project.weather.station', 'Estacion', size=60),
            'dia': fields.integer('Dia Juliano'),
            'tmax': fields.float('T. Max.'),
            'tmin': fields.float('T. Min.'),
            'tmed': fields.float('T. Med.'),
            'hum_max': fields.float('Hum. Max.'),
            'hum_min': fields.float('Hum. Min.'),
            'hum_med': fields.float('Hum. Med.'),
            'vel_viento': fields.float('Vel. Viento'),
            'dir_viento': fields.float('Dir. Viento'),
            'rad': fields.float('Rad. Solor'),
            'precip': fields.float('Precipitaciones'),
            'eto': fields.float('Eto'),
            'fecha': fields.date('Fecha'),
            'htmax': fields.datetime('Hora T. Max.'),
            'htmin': fields.datetime('Hora T. Min.'),
            'fecha_str': fields.char('Fecha Temp', size=60),
            'htmax_str': fields.char('Hora T. Max. Temp', size=10),
            'htmin_str': fields.char('Hora T. Min. Temp', size=10),
    }
agro_project_weather()
