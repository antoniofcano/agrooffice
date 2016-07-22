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

class agro_health_analisis(osv.osv):
    _name = 'agro.health.analisis'
    _description = 'Analisis'
    
    _columns={
        'name': fields.char('Referencia', size=128, required = True),
        'explotacion_id': fields.many2one('agro.project.explotacion', 'Explotacion', required = True),
        'lab_id': fields.many2one('res.partner', 'Laboratorio', ),
        'fecha_muestra': fields.date('Fecha muestra'), 
        'fecha_resultados': fields.date('Fecha resultados'),
        'tipo_id': fields.selection([('0','Vegetal'), ('1','Suelo'), ('2', 'Agua')], 'Tipo', required = True), 
        'product_id': fields.many2one('product.product', 'Variante/LdM'),
        'observaciones': fields.text('Observaciones',  ),
        'responsable_id': fields.many2one('res.users', 'Responsable', required = True),
    }
    
agro_health_analisis()
