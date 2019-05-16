from django.conf.urls import url
from request_app import views

urlpatterns = [
    # 1.路由url的路径传递参数
    # eg: http://127.0.0.1:8000/weather/beijing/2019  通过`正则表达式`提取
    url(r'weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather),
    # 2.查询字符串传递参数
    # eg:http://127.0.0.1:8000/request/user?name=curry&like=basketball
    url(r'user/', views.query_user),
    # 3.请求体传递参数--form表单格式
    # 参数是通过请求体携带，在url路径上看不到   {"name": laowang, "age": 38}
    url(r'^form/$', views.body_form),
    # 4.请求体传递参数---非表单格式数据 json xml text
    # 参数是通过请求体携带，在url路径上看不到   {"name": laowang, "age": 38}
    url(r'^not_form/$', views.body_notform),
    # 5.请求头传递参数
    url(r'^header/$', views.header),
    # 6.HTTPRequest请求对象其他常用属性
    url(r'^others/$', views.others),
]