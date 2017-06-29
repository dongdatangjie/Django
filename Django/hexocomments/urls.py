#coding:utf-8
from django.conf.urls import url

from . import views


app_name = 'hexocomments'
urlpatterns = [

    # 绑定关系的写法是把网址和对应的处理函数作为参数传给 url 函数（第一个参数是网址，
    # 第二个参数是处理函数），另外我们还传递了另外一个参数 name，这个参数的值将作为处理函数
    # index 的别名，这在以后会用到。
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),

]