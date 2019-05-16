from django.conf.urls import url
from response_app import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^json/$', views.json_response, name='json'),
    url(r'^redirect/$', views.redirect_response),
]