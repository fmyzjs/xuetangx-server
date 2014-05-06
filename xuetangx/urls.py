from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xuetangx.views.home', name='home'),
    # url(r'^xuetangx/', include('xuetangx.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^student/', include("student.urls")),
    url(r'^courses/', include("courses.urls")),
)

handler404 = 'xuetangx.views.my_custom_404_view'
handler500 = 'xuetangx.views.my_custom_error_view'
