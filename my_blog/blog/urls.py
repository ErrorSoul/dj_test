#coding: utf:8
from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^post/(\d+)/$', views.posted, name="posted"),
        url(r'^tag/(\w+)/$',views.tag, name="taged"),
        url(r"^add_comment/(\d+)/$", views.add_comment, name="add_comment"),

        )
