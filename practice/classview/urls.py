from django.conf.urls import url
from classview import views

urlpatterns = [
    url(r'register/', views.RegisterView.as_view()),
    url(r'^index/', views.index)
]