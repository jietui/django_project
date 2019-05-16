from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    request.session['name'] = 'laowang'
    request.session['age'] = 35
    request.session.set_expiry(3600)
    return HttpResponse('登录成功，设置session数据成功')


def index(request):
    name = request.session.get('name', '')
    age = request.session.get('age', '')
    return HttpResponse('首页：%s %s' % (name, age))


def login_out(request):
    request.session.flush()
    return HttpResponse('退出登录，删除session数据成功')