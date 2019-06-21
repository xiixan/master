# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.db import *
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger

'''
这个方法为获取题库数据
'''
def question_page_data(request):
    #先获取客户提交的信息
    # 得到页码
    pageno = request.GET.get('page',1)
    tag_param = request.GET.get('tag','')
    level_param = request.GET.get('level','')

    if tag_param != "":
        question_all = Question.objects.filter(tag__name =tag_param);
    if level_param != "":
        # levels = Level.objects.filter(name=level_param)
        question_all = Question.objects.filter(level__name =level_param);
    else:
        question_all = Question.objects.all();
        
    paginator = Paginator(question_all, 10)
    try:
        page = int(request.GET.get('page', pageno))
        question_all = paginator.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        question_all = paginator.page(1)
        pass

    return question_all

def question_data(request):
    cid = request.GET.get('cid',1)
    quesiton_pk = Question.objects.get(id=cid)
    return quesiton_pk

def tags_all_data(request):
    tag_all = Tag.objects.all();
    return tag_all

def levels_all_data(request):
    levels_all = Level.objects.all();
    return levels_all