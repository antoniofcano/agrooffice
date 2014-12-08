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

class agro_project_pesada(osv.osv):    
    _name = 'agro.project.pesada'
    _description = 'Registra pesadas'
    
    def _calc_task_hours(self, cr, uid, ids, fields_list, args, context=None):
        vals = {}
        task_obj = self.pool.get('project.task')

        work_date_fmt = '%Y-%m-%d %H:%M:%S'
        pesada_date_fmt = '%Y-%m-%d'

        for pesada in ids:
            pesada_data = self.browse(cr, uid, pesada, context)
            pesada_task_id = pesada_data.tarea_id.id

            task_works = task_obj.browse(cr, uid, pesada_task_id, context).work_ids
            hours = 0

            for work in task_works:
                work_date_time = datetime.datetime.strptime(work.date, work_date_fmt)
                work_date = datetime.date(work_date_time.year, work_date_time.month, work_date_time.day)

                pesada_date_time = datetime.datetime.strptime(pesada_data.fecha_recoleccion, pesada_date_fmt)
                pesada_date = datetime.date(pesada_date_time.year, pesada_date_time.month, pesada_date_time.day)

                if pesada_date == work_date:
                    hours = hours + work.hours

            vals[pesada] = hours
        return vals

    def _calc_hours_kilo(self, cr, uid, ids, fields_list, args, context=None):
        vals = {}

        for pesada in ids:
            pesada_data = self.browse(cr, uid, pesada, context)
            vals[pesada] = float(pesada_data.horas) / float(pesada_data.kilos)

        return vals


    _columns={
            'name': fields.integer('Num. de pesada', required = True),
            'campana_id': fields.many2one('project.project', 'Campana', required = True),
            'tarea_id': fields.many2one('project.task', 'Tarea', required = True),
            'fecha_recoleccion': fields.date('Fecha recoleccion', select='1', required= True),
            'fecha_pesada': fields.date('Fecha pesada', select='1', required= True),
            'kilos': fields.float('Kilos', required = True),
            'suciedad': fields.integer('Suciedad (%)'),
            'rendimiento': fields.float('Rendimiento'),
            'horas': fields.function( _calc_task_hours, method=True, store=True, type='float', string='Horas'),
            'horas_kilo': fields.function( _calc_hours_kilo, method=True, store=True, type='float', string='Horas/Kilo'),
              }
    
    _defaults={
            'fecha_recoleccion': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
            'fecha_pesada': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
            'rendimiento': 0,
            'kilos': 0,
    }

agro_project_pesada()
