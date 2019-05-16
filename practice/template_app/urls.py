from django.conf.urls import url
from template_app import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^index_child/$', views.index_child),
    url(r'^jinja2/$', views.jinja2),
]