from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    response = HttpResponse(content="登录成功-设置cookie成功")
    response.set_cookie("name", "laowang")
    response.set_cookie("is_login", "True")
    return response