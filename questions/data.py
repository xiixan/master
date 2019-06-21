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
    tag_param = request.GET.get('tag',None)
    level_param = request.GET.get('level',None)
    title_param = request.GET.get('title',None)
    if title_param:
        question_all = Question.objects.filter(title__contains =title_param);
    elif tag_param:
        question_all = Question.objects.filter(tag__name =tag_param);
        question_all = question_all.values().distinct()
    elif level_param:
        # levels = Level.objects.filter(name=level_param)
        question_all = Question.objects.filter(level__name =level_param);
    else:
        question_all = Question.objects.all();
        
    paginator = Paginator(question_all, 10)
    try:
        page = int(request.GET.get('page', 1))
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

def comments_user_data(request):
    user = request.user
    levels_user = Comment.objects.filter(user=user);
    paginator = Paginator(levels_user, 10)
    try:
        page = int(request.GET.get('page', 1))
        levels_user = paginator.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        levels_user = paginator.page(1)
        pass

    return levels_user