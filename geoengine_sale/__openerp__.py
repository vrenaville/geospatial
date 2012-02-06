# -*- encoding: utf-8 -*-
##############################################################################
#
#    Author Nicolas Bessi. Copyright Camptocamp SA
##############################################################################
{'name': 'Geospatial support for sales',
 'version': '0.1',
 'category': 'GeoBI',
 'description': """Add geo_point on partner and addresses
 point on partner is function field that return geo point of 
 """,
 'update_xml': ['geo_sale_view.xml'],
 'author': 'Camptocamp',
 'website': 'http://openerp.camptocamp.com',
 'depends': ['base', 'geoengine_partner', 'sale'],
 'installable': True,
 'application': True,
 'active': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: