from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

# Create your views here.


def index(request):
    url = reverse('users:index')
    print(url)
    return HttpResponse('hello world')