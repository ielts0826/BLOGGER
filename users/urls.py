# users/urls.py
from django.urls import path
from . import views

app_name = 'users' # 定义应用命名空间
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
        ]