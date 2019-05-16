from django.conf.urls import url
from session_app import views

urlpatterns = [
    url(r'^login/', views.login),
    url(r'index/', views.index),
    url(r'^login_out/', views.login_out)
]