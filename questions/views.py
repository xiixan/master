# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render,redirect
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from models import *
from forms import *
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import PermissionDenied
from data import *
from admin import *

# Create your views here.
def index(request):
    question_all = question_page_data(request)
    tags_all = tags_all_data(request)
    levels_all = levels_all_data(request)
    return render(request,"index.html",locals())

def questions(request):
    question_all = question_page_data(request)
    return render(request,"questions.html",locals())

def question_detail(request):
    try:
        question = question_data(request)
    except Question.DoesNotExist as e:
        print e
        return render(request, 'failure.html', {'reason': '没有找到对应的文章'})

    if request.user.is_authenticated():
        user = request.user
        # if user.level != question.level.level:
        #     raise PermissionDenied

    # 评论表单
        comment_form = CommentForm({'author': request.user.username,
                                    'email': request.user.email,
                                    'question': question.id})
    else:
        raise PermissionDenied
    # 获取评论信息
    comments = Comment.objects.filter(question=question).order_by('id')
    comment_list = []
    for comment in comments:
        print comment.content
        for item in comment_list:
            if not hasattr(item, 'children_comment'):
                setattr(item, 'children_comment', [])
            if comment.pid == item:
                item.children_comment.append(comment)
                break
        if comment.pid is None:
            comment_list.append(comment)
    return render(request,"question_detail.html",locals())

def change_comment(request):
    CommentAdmin.changeform_view
    pass

# 注销
def do_logout(request):
    try:
        logout(request)
    except Exception as e:
        print e
        pass
    return redirect(request.META['HTTP_REFERER'])

# 注册
def do_reg(request):
    try:
        if request.method == 'POST':
            reg_form = RegForm(request.POST)
            if reg_form.is_valid():
                # 注册
                user = User.objects.create(username=reg_form.cleaned_data["username"],
                                    email=reg_form.cleaned_data["email"],
                                    password=make_password(reg_form.cleaned_data["password"]),)
                user.save()

                # 登录
                user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式
                login(request, user)
                return redirect(request.POST.get('source_url'))
            else:
                return render(request, 'failure.html', {'reason': reg_form.errors})
        else:
            reg_form = RegForm()
    except Exception as e:
        print e
        pass
    return render(request, 'reg.html', locals())

# 登录
def do_login(request):
    try:
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                # 登录
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user is not None:
                    user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式
                    login(request, user)
                else:
                    return render(request, 'failure.html', {'reason': '登录验证失败'})
                return redirect(request.POST.get('source_url'))
            else:
                return render(request, 'failure.html', {'reason': login_form.errors})
        else:
            login_form = LoginForm()
    except Exception as e:
        pass
    return render(request, 'login.html', locals())

def comment_post(request):
    print "enter comment post"
    try:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            #获取表单信息
            comment = Comment.objects.create(username=comment_form.cleaned_data["author"],
                                             email=comment_form.cleaned_data["email"],
                                             content=comment_form.cleaned_data["comment"],
                                             question_id=comment_form.cleaned_data["question"],
                                             user=request.user if request.user.is_authenticated() else None)
            comment.save()
            print "comment is success be saved!!!"
        else:
            return render(request, 'failure.html', {'reason': comment_form.errors})
    except Exception as e:
        print "exception is happend";
        return e
    return redirect(request.META['HTTP_REFERER'])


def category(request):
    try:
        # 先获取客户端提交的信息
        cid = request.GET.get('cid', None)
        try:
            category = Category.objects.get(pk=cid)
        except Category.DoesNotExist:
            return render(request, 'failure.html', {'reason': '分类不存在'})
        # article_list = Article.objects.filter(category=category)
        # article_list = getPage(request, article_list)
        category_list = Category.objects.all()
    except Exception as e:
        logger.error(e)
    return render(request, 'category.html', locals())

def comment(request):
    return render(request,"comment.html",locals())
def moodList(request):
    return render(request,"moodList.html",locals())
def article(request):
    return render(request,"article.html",locals())