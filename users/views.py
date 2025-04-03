from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') # 注册成功后跳转到登录页面
    template_name = 'registration/signup.html' # 指定模板文件
