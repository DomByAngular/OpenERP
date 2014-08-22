#!/usr/bin/python
# -*-coding:utf-8 -*-
# add by yangshuang on 2014-8-20

from openerp.osv import osv,fields
import time

class canyou_student(osv.osv):
    _name = 'canyou.student'
    _description = u'demo学生实体'
    _columns = {
    'name':fields.char( u'学生姓名',size=64,select=True),
    'age':fields.integer(u'学生年龄',select=True),
    'gender':fields.selection([(1,'男'),(2,'女')],u'学生性别'),
    # 'gender':fields.integer(u'学生性别(1男2女)'),
    'class':fields.char(u"班级"),
    'student_no':fields.char(u'学号',size=10),
    'major':fields.char(u'所学专业',size=24),
    'birthday':fields.datetime(u'出生日期'),
    'email':fields.char(u'电子邮件',size=20),
    'scores':fields.one2many('canyou.student.lesson.scores','student_id',u'学分',ondelete='cascade')
    }
    _defaults={
        'birthday': lambda *a:time.strftime('%Y-%m-%d %H:%M:%S'),
        'gender':lambda *a:1
    }

    def get_student_total_scores(self,cr,uid,ids,name,args,context=None):
        '''
        获取学生的总成绩
        '''
    pass
canyou_student()


