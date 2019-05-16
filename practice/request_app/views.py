from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
def weather(request, city, year):
    '''1.路由url的路径传递参数'''
    return HttpResponse('路由url的路径传递参数 城市: %s 年份: %s' % (city, year))

def query_user(request):
    param_dict = request.GET
    print(request.GET)
    print(type(request.GET))
    name = param_dict.get('name', 'haha')
    age = param_dict.getlist('age')
    return HttpResponse('查询字符串传递参数：%s %s' % (name, age))


def body_form(request):
    param_dict = request.POST
    print(request.POST)
    print(type(request.POST))
    name = param_dict.get('name', '')
    age = param_dict.get('age', '')
    return HttpResponse('请求体传递参数--form表单格式：%s %s' % (name, age))


def body_notform(request):
    b_data = request.body
    print(type(b_data))
    json_str = b_data.decode()
    print(type(json_str))
    my_dict = json.loads(json_str)
    print(type(my_dict))
    return HttpResponse('请求体传递参数---非表单格式数据：%s' % my_dict)


def header(request):
    dict = request.META
    content_type = dict.get('CONTENT_TYPE', '')
    return HttpResponse('请求头传递参数：%s' % content_type)


def others(request):
    method = request.method
    print(method)
    user = request.user
    print(user)
    path = request.path
    print(path)
    encoding = request.encoding
    print(encoding)
    files = request.FILES
    return HttpResponse('6.HTTPResponse请求对象其他常用属性')