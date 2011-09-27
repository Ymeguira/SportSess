from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import *

urlpatterns = patterns('Main.views',
    # Examples:
    # url(r'^$', 'SportSess.views.home', name='home'),
    # url(r'^SportSess/', include('SportSess.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^home/$', 'home'),
    url(r'^$', 'login'),
    
)
