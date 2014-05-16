from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
    url(r'^selected/$', views.selected),
    url(r'^upcoming/$', views.upcoming),
    url(r'^current/$', views.current),
    url(r'^past/$', views.past),
    url(r'^categories/$', views.categories),
    url(r'^search/$', views.search),
    url(r'^unenroll/$', views.unenroll),
    url(r'^enroll/$', views.enroll),
    url(r'^lectures/$', views.lectures),
    url(r'^lecture/$', views.lecture),
    url(r'^ware/$', views.ware),
    url(r'^video/$', views.video),
)









