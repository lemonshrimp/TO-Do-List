from django.conf.urls import patterns, url, include
from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()
 
urlpatterns = patterns('',
    url(r'^$', 'tdl.views.index'),
    url(r'^admin/',include(admin.site.urls)),
)
