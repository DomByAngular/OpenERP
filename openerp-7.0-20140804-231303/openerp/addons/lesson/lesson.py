#!/usr/bin/python
# coding=utf-8

from openerp.osv import fields, osv
#定义课程对象信息
class canyou_lesson(osv.osv):
    # _name _columns字段必须，其他可选
    _name = 'canyou.lesson'
    _description = u'课程管理'
    _columns = {
    'name':fields.char( u'课程名',size=64,select=True),
    'date_start':fields.date(u'开始日期',select=True),
    'total_day':fields.float(u'总天数',digits=(16,1)),
    'teacher':fields.many2one('res.users',u'授课老师'),
    'students':fields.many2many('canyou.student',
                                'canyou_lessons_students',
                                'lesson_id',
                                'student_id',
                                '选课的学生'),
    'lesson_scores':fields.one2many("canyou.student.lesson.scores",'lesson_id',u'课程学分')
}
canyou_lesson()


class canyou_student_lesson_scores(osv.osv):
    '''
       定义学生课程分数表
    '''
    _name='canyou.student.lesson.scores'
    _description=u'学分管理'
    _columns={
        'student_id':fields.many2one('canyou.student',u'学号'),
        'lesson_id':fields.many2one('canyou.lesson',u'课程号'),
        'score':fields.float(u'成绩',digits=(3,1))
    }
canyou_student_lesson_scores()
