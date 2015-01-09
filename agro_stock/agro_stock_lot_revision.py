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
import time
import datetime

import logging

_logger = logging.getLogger(__name__)


class agro_stock_lot(osv.osv):
    _inherit = 'stock.production.lot'

    def _get_rdto(self, cr, uid, ids, fields_list, args, context=None):
        vals = {}

        for lot in ids:
            lot_data = self.browse(cr, uid, lot, context)
            value = 0.0
            
            for revision in lot_data.revisions:
                if revision.type_id.name == 'Rendimiento':
                    value = float(revision.value) or 0.0

            vals[lot] = value

        return vals

    def _get_acidez(self, cr, uid, ids, fields_list, args, context=None):
        vals = {}

        for lot in ids:
            lot_data = self.browse(cr, uid, lot, context)
            value = 0.0

            for revision in lot_data.revisions:
                if revision.type_id.name == 'Acidez':
                    value = float(revision.value) or 0.0

            vals[lot] = value

        return vals

    def _get_suciedad(self, cr, uid, ids, fields_list, args, context=None):
        vals = {}

        for lot in ids:
            lot_data = self.browse(cr, uid, lot, context)
            value = 0.0

            for revision in lot_data.revisions:
                if revision.type_id.name == 'Suciedad':
                    value = float(revision.value) or 0.0

            vals[lot] = value

        return vals

    _columns={
            'revisions': fields.one2many('agro.stock.production.lot.revision', 'lot_id', 'Revisions'),
            'rendimiento': fields.function( _get_rdto, method=True, store=False, type='float', string='Rendimiento graso(%)'),
            'acidez': fields.function( _get_acidez, method=True, store=False, type='float', string='Acidez(%)'),
            'suciedad': fields.function( _get_suciedad, method=True, store=False, type='float', string='Suciedad(%)'),
    }

agro_stock_lot()

class agro_stock_production_lot_revision(osv.osv):
    _name = 'agro.stock.production.lot.revision'
    _description = 'Serial Number Revision'

    _columns = {
        'name': fields.char('Revision Name', size=64, required=True),
        'description': fields.text('Description'),
        'date': fields.date('Revision Date'),
        'indice': fields.char('Revision Number', size=16),
        'author_id': fields.many2one('res.users', 'Author'),
        'lot_id': fields.many2one('stock.production.lot', 'Serial Number', select=True, ondelete='cascade'),
        'type_id': fields.many2one('agro.stock.production.lot.revision.type', 'Tipo de observacion'),
        'value': fields.float('Cantidad', ),
    }

    _defaults = {
        'author_id': lambda x, y, z, c: z,
        'date': fields.date.context_today,
    }


agro_stock_production_lot_revision()

class agro_stock_lot_revision_type(osv.osv):
    _name = 'agro.stock.production.lot.revision.type'
    _description = 'Tipo de observacion'

    _columns = {
        'name': fields.char('Tipo de observacion', size=15, required=True),
    }

agro_stock_lot_revision_type()

