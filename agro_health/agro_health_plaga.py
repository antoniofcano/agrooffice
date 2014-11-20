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

class agro_health_plaga(osv.osv):
    _name = 'agro.health.plaga'
    _description = 'Plagas'
    
    _columns={
        'name': fields.char('Nombre', size=128, required = True),
        'sci': fields.char('Nombre cientifico', size=128,),
        'tipo': fields.selection([('0','Plaga'), ('1','Enfermedad')], 'Tipo'), 
        'cultivo_id': fields.many2one('agro.project.cultivo', 'Cultivo asociado'),
        'descripcion': fields.text('Descripcion',  ),
        'activa': fields.many2many('agro.health.plaga', 'agro_plaga_activa', 'plaga_id', 'activa_id', 'Materia activa asociada'),
    }
    
agro_health_plaga()


class agro_health_activa(osv.osv):
    _name = 'agro.health.activa'
    _description = 'Materia Activa'

    _columns={
        'name': fields.char('Materia Activa', size=128, required = True),
        'plaga': fields.many2many('agro.health.plaga', 'agro_plaga_activa', 'activa_id', 'plaga_id', 'Plagas asociada'),
        'product_ids': fields.one2many('agro.health.product', 'materia_id', 'Productos'),
    }

agro_health_activa()

class agro_health_product(osv.osv):
    _name = 'agro.health.product'
    _description = 'Producto fitosanitario'

    _columns={
        'name': fields.char('Nombre', size=128, required = True),
        'num': fields.integer('N. Registro', required = True),
        'titular': fields.char('Titular', size=128, required = True),
        'materia_id': fields.many2one('agro.health.activa', 'Materia activa', required = True),
        'product_id': fields.many2one('product.product', 'Producto comercial'),
    }
agro_health_product()
