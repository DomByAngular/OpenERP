#！-*- coding=utf-8 -*-
__author__ = 'ys'

from openerp.osv import fields, osv

class oecn_training_lesson(osv.osv):
    _inherit = 'oecn.training.lesson' #要继承的对象的_name
    _columns = {
    'classroom_id':fields.many2one('oecn.training.classroom','教室'),#添加一个教室属性，为多对一对象。
}
oecn_training_lesson()

    # vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
