from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View


# Create your views here.


def my_decorator(func):
    def wrapper(request, *args, **kwargs):
        print('装饰器被调用了')
        print(request.method)
        return func(request, *args, **kwargs)
    return wrapper


# 方法二
# class Decorator(object):
#     def __init__(self, fn):
#         self.__fn = fn
#
#     def __call__(self, request, *args, **kwargs):
#         print('装饰器被调用了')
#         print(request.method)
#         return self.__fn(self, request)


@method_decorator(my_decorator, 'dispatch')
class RegisterView(View):
    """类视图"""

    # @Decorator
    def get(self, request):
        return HttpResponse('展示注册页面')

    def post(self, request):
        return HttpResponse('注册业务逻辑判断')


def index(request):
    print('index----------')
    return HttpResponse('index----------')
