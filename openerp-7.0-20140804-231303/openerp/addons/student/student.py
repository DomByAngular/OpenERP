#!/usr/bin/python
# -*-coding:utf-8 -*-
# add by yangshuang on 2014-8-20

from openerp.osv import osv,fields
import time
from openerp import  tools

class canyou_student(osv.osv):
    _name = 'canyou.student'
    _description = u'demo学生实体'
    _columns = {
    'name':fields.char( u'学生姓名',size=64,select=True),
    'age':fields.integer(u'学生年龄',select=True),
    'gender':fields.selection([(1,'男'),(2,'女')],u'学生性别'),
    'image': fields.binary("头像",
            help="员工头像，分辨率限制为1024x1024px."),
    'image_medium': fields.function(_get_image, fnct_inv=_set_image,
        string="头像(中)", type="binary", multi="_get_image",
        store = {
            'canyou.student': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
        },
    help="自动生成，用于看板视图，分辨率128*128."),
    'image_small': fields.function(_get_image, fnct_inv=_set_image,
        string="头像(小)", type="binary", multi="_get_image",
        store = {
            'canyou.student': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
        },
        help="自动生成，用于需要显示小头像的地方"),
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

    def _get_image(self, cr, uid, ids, name, args, context=None):
        result = dict.fromkeys(ids, False)
        for obj in self.browse(cr, uid, ids, context=context):
            result[obj.id] = tools.image_get_resized_images(obj.image)
        return result

    def _set_image(self, cr, uid, id, name, value, args, context=None):
        return self.write(cr, uid, [id], {'image': tools.image_resize_image_big(value)}, context=context)
canyou_student()


