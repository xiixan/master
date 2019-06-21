# -*- coding: utf-8 -*-
from django import template
from questions.models import LevelEnums
register = template.Library()

# 定义一个将日期中的月份转换为大写的过滤器，如8转换为八
@register.filter
def level_convert(key):
    return 111
        # return LevelEnums.LEVEL_IN_USER_CHOICES[key]
register.filter('month_to_upper', level_convert)