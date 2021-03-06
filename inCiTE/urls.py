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
    url(r'^idea/$', 'core.views.idea', name='idea'),
    url(r'^board/$', 'core.views.board', name='board'),
    url(r'^test1/$', 'core.views.test1', name='test1'),
    url(r'^test2/$', 'core.views.test2', name='test2'),
    url(r'^start1/$', 'core.views.start1', name='start1'),
    url(r'^start2/$', 'core.views.start2', name='start2'),
    url(r'^clicklike/(?P<uid>\d+)/(?P<lid>\d+)$', 'core.views.clicklike', name='clicklike'),
    url(r'^newseek/$', 'core.views.newseek', name='newseek'),

    url(r'^admin/', include(admin.site.urls)),
)
