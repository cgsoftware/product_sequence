# -*- encoding: utf-8 -*-

from osv import osv, fields

class product_product(osv.osv):
    _inherit = 'product.product'

    def create(self, cr, uid, vals, context={}):
        #import pdb;pdb.set_trace()
        if  (not 'default_code' in vals) or vals.get('default_code',True) or vals.get('default_code',True)==False:
            if 'codice_template' in vals:
                vals['default_code'] = vals['codice_template']+self.pool.get('ir.sequence').get(cr, uid, 'product.product')
            else:
                vals['default_code'] = self.pool.get('ir.sequence').get(cr, uid, 'product.product')
        return super(product_product, self).create(cr, uid, vals, context)
product_product() 

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
