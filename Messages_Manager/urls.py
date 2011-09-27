from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('Messages_Manager.views',
    # Examples:
    # url(r'^$', 'SportSess.views.home', name='home'),
    # url(r'^SportSess/', include('SportSess.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', 'messages_index'),
    url(r'compose/$', 'compose'),
    url(r'send/$', 'send'),
    url(r'save/$', 'save'),
    url(r'delete/$', 'delete'),
    

)
