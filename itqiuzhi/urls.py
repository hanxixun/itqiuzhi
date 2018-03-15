# -*- coding: utf-8 -*-
"""itqiuzhi URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

from django.views.static import serve  # 模板文件图片解析模块

from interview.views import InterListView, InterDetails, RegView, LoginView, LogoutView, IndexView  # 导入Views函数/类
from itqiuzhi.settings import MEDIA_ROOT  # 媒体文件图片解析路径

urlpatterns = [
    url(r'^admin/', admin.site.urls),  # 后台管理映射
    url(r'^$', IndexView.as_view(), name="index"),  # 首页映射
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),  # 管理媒体文件路径和处理模块
    url(r'^interlist/$', InterListView.as_view(), name="interlist"),  # 求职详情列表页映射
    url(r'^interdetail/(?P<interview_id>\d+)/$', InterDetails.as_view(), name="interdetail"),  # 招聘详情页
    url(r'^ueditor/', include('DjangoUeditor.urls')),  # 增加ueditor映射
    url(r'^register/$', RegView.as_view(), name="register"),  # 用户注册页映射
    url(r'^login/$', LoginView.as_view(), name="login"),  # 用户登录页面映射
    url(r'^logout/$', LogoutView.as_view(), name="logout"),  # 用户注销页面映射
]
