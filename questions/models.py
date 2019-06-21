# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField
# Create your models here.

# 用户模型.
# 第一种：采用的继承方式扩展用户信息（本系统采用）
# 扩展：关联的方式去扩展用户信息
class User(AbstractUser):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    LEVEL_IN_USER_CHOICES = (
        (ONE, '青铜'),
        (TWO, '白银'),
        (THREE, '黄金'),
        (FOUR, '大佬'),
    )
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200, blank=True, null=True, verbose_name='用户头像')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')
    level = models.IntegerField(blank=True, null=True, verbose_name='等级',choices=LEVEL_IN_USER_CHOICES,
        default=ONE,)
    num = models.IntegerField(blank=True, null=True, verbose_name='答题数量')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username

    #标签
class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='题目标签')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=30, verbose_name='题目级别')

    class Meta:
        verbose_name = '级别'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

# question模型
class Question(models.Model):
    title = models.CharField(max_length=50, verbose_name='Question背景')
    desc = models.CharField(max_length=50, verbose_name='Question描述')
    content = HTMLField('Question描述')#models.TextField(verbose_name='Question内容')
    successCount = models.IntegerField(default=0, verbose_name='成功次数')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(User, verbose_name='用户')
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    level = models.ForeignKey(Level, blank=True, null=True, verbose_name='级别')

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return self.title

# 分类
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称')
    index = models.IntegerField(default=999,verbose_name='分类的排序')


    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.name
# 评论模型
class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    username = models.CharField(max_length=30, blank=True, null=True, verbose_name='用户名')
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='邮箱地址')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='用户')
    question = models.ForeignKey(Question, blank=True, null=True, verbose_name='题目')
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name='父级评论')
    isSuccess = models.NullBooleanField(blank=True, null=True, verbose_name='是否正确')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str(self.id)


