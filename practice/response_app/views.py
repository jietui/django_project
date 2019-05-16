from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.


def index(request):
    response = HttpResponse()
    response.content = "我是响应内容--操作对象"
    response.status_code = 200
    response['Content-Type'] = 'application/json'
    response['itcast'] = 'python'
    return response


def json_response(request):
    my_dict = {
        "name": "durant",
        "age": "30"
    }
    return JsonResponse(my_dict)


def redirect_response(request):
    url = reverse('json')
    return redirect(url)