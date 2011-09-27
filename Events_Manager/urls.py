from django.conf.urls.defaults import patterns, include, url



urlpatterns = patterns('Events_Manager.views',
    # Examples:
    # url(r'^$', 'SportSess.views.home', name='home'),
    # url(r'^SportSess/', include('SportSess.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', 'index'),
    url(r'^create/$', 'create'),
    url(r'^publish/$', 'publish'),
    url(r'^search/$', 'search'),
    url(r'^detail/(?P<event_id>\d+)/$', 'detail'),
    url(r'^result/$', 'result'),
)
