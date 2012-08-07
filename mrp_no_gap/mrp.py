# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#    Copyright (C) 2012-2012 Camptocamp Austria (<http://www.camptocamp.at>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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


from osv import fields, osv
import logging

class mrp_production(osv.osv):
    _inherit = "mrp.production"

    _defaults = {
	 'name' : '/',
        }

    def create(self, cr, uid, vals, context=None):
        if vals.get('name', '/') == '/':
            vals.update({'name':  self.pool.get('ir.sequence').get(cr, uid, 'mrp.production')})
        return super(mrp_production, self).create(cr, uid, vals, context=context)

mrp_production()

    
