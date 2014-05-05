from django.conf.urls import patterns, url

from student import views

urlpatterns = patterns('',
    url(r'^verify/$', views.verify),
    url(r'^info/$', views.info),
)
