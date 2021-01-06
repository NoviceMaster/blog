# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : NoviceMaster
# @Email   : mrchenbin@126.com
# @Time    : 2021/1/6 17:12 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url, include
from django.views.static import serve
from rest_framework import routers

from blog import settings
from .views import UserViewSet

router = routers.DefaultRouter()  # 开发环境用，有主界面
# router = routers.SimpleRouter() # 生产环境用

router.register('user', UserViewSet)

urlpatterns = [
    url(r'^user/', UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    url('', include(router.urls)),
    url(r'avatar/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
