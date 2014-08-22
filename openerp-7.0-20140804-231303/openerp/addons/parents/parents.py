#!/usr/bin/python
# -*- coding:utf-8 -*-

from openerp.osv import osv,fields


class canyou_parents(osv.osv):
    '''
        define parents class
    '''
    _name='canyou.parents'
    _description=u'家长实体'
    _columns={
        'name':fields.char(u'家长姓名',size=12,select=True),
        'email':fields.char(u'联系电邮',size=24),
        'address':fields.char(u'联系地址',size=50),
        'telephone':fields.char(u'联系电话',size=11),
        'student':fields.many2many('canyou.student','student_parents_ref',
                                   'student_id','parent_id',u'家长所监护的学生')
    }
canyou_parents()

