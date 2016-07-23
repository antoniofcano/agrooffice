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

class agro_health_plaga(osv.osv):
    _name = 'agro.health.plaga'
    _description = 'Plagas'
    
    _columns={
        'name': fields.char('Nombre', size=128, required = True),
        'sci': fields.char('Nombre cientifico', size=128,),
        'tipo': fields.selection([('0','Plaga'), ('1','Enfermedad')], 'Tipo'), 
        'cultivo_id': fields.many2one('agro.project.cultivo', 'Cultivo asociado'),
        'descripcion': fields.text('Descripcion',  ),
    }
    
agro_health_plaga()
