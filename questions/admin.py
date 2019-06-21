# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.contrib import admin

class UserAdmin(admin.ModelAdmin):
    exclude = [('num')]
class CommentAdmin(admin.ModelAdmin):
    # 修改是否正确时，修改问题中正确数目
    def change_view(self, request, object_id, form_url='', extra_context=None):
        if request.method == 'POST':
            isSuccess=request.POST.get('isSuccess','')
            if isSuccess > 1:
                comment = Comment.objects.get(id=object_id)
                isSuccess_True_False = False
                if isSuccess == '2':
                        isSuccess_True_False = True
                print isSuccess_True_False != comment.isSuccess
                if isSuccess_True_False != comment.isSuccess:
                    question = comment.question
                    successCount = question.successCount
                    if isSuccess == '2':
                        question.successCount += 1
                    else:
                        question.successCount = successCount-1 if successCount > 0 else successCount 
                    question.save()
        return self.changeform_view(request, object_id, form_url, extra_context)


# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Tag)
admin.site.register(Level)
admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)
# admin.site.register(Links)
# admin.site.register(Ad)