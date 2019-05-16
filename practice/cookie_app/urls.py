from django.conf.urls import url
from cookie_app import views

urlpatterns = [
    url(r'login/$', views.login),
]