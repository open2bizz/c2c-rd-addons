# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#    Copyright (C) 2010-2010 Camptocamp Austria (<http://www.camptocamp.at>)
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
{ 'name'        : 'Adds fields for invoice creation'
, 'version'     : '0.7'
, 'category'    : 'Sales Management'
, 'description' : """
This module will add
 * invoice date
 * modified description/reference (free text + analytic account name)
"""
, 'author'      : 'Camptocamp Austria'
, 'depends'     : [ 'hr_timesheet_invoice' ]
, 'update_xml'  : ['wizard/hr_timesheet_invoice_create_view.xml']
, 'demo_xml'    : []
, 'installable' : True
, 'active'      : False
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
