"""master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from questions.views import *
from tinymce.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^tinymce/', include('tinymce.urls')),
    # url(r'^archive/', archive),
    # url(r'^archive/$', archive, name='archive'),
    # url(r'^article/$', article, name='article'),
    # url(r'^comment/post/$', comment_post, name='comment_post'),
    url(r'^logout$', do_logout, name='logout'),
    url(r'^reg', do_reg, name='reg'),
    url(r'^login', do_login, name='login'),
    url(r'^moodList', moodList, name='moodList'),
    url(r'^comment/post/$', comment_post, name='comment_post'),
    url(r'^comment', comment, name='comment'),
    url(r'^question_detail', question_detail, name='question_detail'),
    url(r'^questions', questions, name='questions'),
    url(r'^category/$', category, name='category'),
]
