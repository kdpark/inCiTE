from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^about/$', 'core.views.about', name='about'),
    url(r'^contact/$', 'core.views.contact', name='contact'),
    url(r'^member/$', 'core.views.member', name='member'),
    url(r'^relation/$', 'core.views.relation', name='relation'),
    url(r'^calendar/$', 'core.views.calendar', name='calendar'),


    url(r'^admin/', include(admin.site.urls)),
)
