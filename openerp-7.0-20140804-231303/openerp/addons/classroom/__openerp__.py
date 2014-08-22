#！-*- coding=utf-8 -*-

    # -*- coding: utf-8 -*-
    # name: 模块名
    #version: 模块版本
    #description:模块说明
    #author:作者
    #website:网址
    #depends:#依赖的模块,此模块我们会继承oecn_training所以必须依赖他
    #update_xml:模块更新的时候会读入的文件 #需要继承的视图
    #installable:可否安装
    #category:模块类型
{
    "name" : "培训教室",
    "version" : "1.0",
    "description" : "OECN Training Demo -- ClassRoom",
    "author" : "Shine IT",
    "website" : "http://www.openerp.cn",
    "depends" : ['oecn_training'],
    "update_xml" : [
    "lesson_view.xml" ,
    "classroom_view.xml",],
    "installable" : True,
    "category":"Generic Modules/Others"
}
