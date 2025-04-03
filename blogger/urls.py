"""
URL configuration for blogger project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include # 确保导入 include

urlpatterns = [
    path("admin/", admin.site.urls),
    # 添加下面这行，将 /accounts/ 开头的 URL 指向 Django 内建的认证 URL
    path('accounts/', include('django.contrib.auth.urls')),
    # 添加下面这行，将用户注册的 URL 指向我们即将创建的 users 应用的 URL
    path('accounts/', include('users.urls')), # 我们将注册 URL 放在 users 应用里
    # 稍后我们会把博客相关的 URL 放在这里
    path('', include('blog.urls')), # 添加博客应用的 URL
]
