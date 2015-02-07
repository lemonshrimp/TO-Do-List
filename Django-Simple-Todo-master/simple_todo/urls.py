from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'todo.views.index'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^todos/', include('todo.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', 'todo.views.register'),
    
)
