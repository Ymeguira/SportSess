from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf.urls.defaults import patterns, include, url

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SportSess.views.home', name='home'),
    # url(r'^SportSess/', include('SportSess.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),  
    
    url(r'^SportSess/$', include('Main.urls')),
    url(r'^SportSess/fields/', include('Fields_Manager.urls')),
    
    url(r'^SportSess/messages/', include('messages.urls')),
    
    url(r'^SportSess/Events_Manager/', include('Events_Manager.urls')),

    
    url(r'^SportSess/home/$', 'SportSess.Main.views.home'),
    url(r'^SportSess/authentication/$', 'SportSess.Users_Manager.views.authentication'),
    url(r'^SportSess/logout/$', 'SportSess.Users_Manager.views.logout'),
    url(r'^SportSess/profil/$', 'SportSess.Users_Manager.views.profil'),
    url(r'^SportSess/friends/$', 'SportSess.Users_Manager.views.friends_list'),
    url(r'^SportSess/sign_up/$', 'SportSess.Users_Manager.views.sign_up'),
    
     url(r'^SportSess/messages/', include('Messages_Manager.urls')),
)
