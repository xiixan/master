# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.contrib import admin

# Register your models here.
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Level)
admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Comment)
# admin.site.register(Links)
# admin.site.register(Ad)