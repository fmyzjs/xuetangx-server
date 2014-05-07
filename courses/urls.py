from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
    url(r'^selected/$', views.selected),
    url(r'^upcoming/$', views.upcoming),
    url(r'^current/$', views.current),
    url(r'^past/$', views.past),
    url(r'^categories/$', views.categories),
    url(r'^search/$', views.search),
    url(r'^about/$', views.about),
    url(r'^info/$', views.info),
    url(r'^ware/$', views.ware),
)









