#!/usr/bin/python
# -*- coding:utf-8 -*-

# name: 模块名
#version: 模块版本
#description:模块说明
#author:作者
#website:网址
#depends:依赖的模块
#update_xml:模块更新的时候会读入的文件
#installable:可否安装
#category:模块类型

{
    "name" : "家长管理",
    "version" : "1.0",
    "description" : '家长管理模块',
    "author" : "yangshuang",
    "website" : "http://www.canyousoftware.com",
    "depends" : ["student"],
    "update_xml" : ["parents_view.xml"],
    "installable" : True,
    "category":'Generic Modules/Others'
}