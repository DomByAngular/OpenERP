#!/usr/bin/python
# -*-coding:utf-8 -*-
# add by yangshuang on 2014-8-20

from openerp.osv import osv,fields

class canyou_student(osv.osv):
    _name = 'canyou.student'
    _description = u'demo学生实体'
    _columns = {
    'name':fields.char( u'学生姓名',size=64,select=True),
    'age':fields.integer(u'学生年龄',select=True),
    'gender':fields.integer(u'学生性别(1男2女)'),
    'classq':fields.char(u"类别"),
    'birthday':fields.datetime(u'出生日期'),
    'email':fields.char(u'电子邮件',size=20),
    }
canyou_student()


