from django.conf.urls.defaults import patterns, include, url



urlpatterns = patterns('Users_Manager.views.',
    # Examples:
    # url(r'^$', 'SportSess.views.home', name='home'),
    # url(r'^SportSess/', include('SportSess.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    """url(r'^SportSess/authentication/$', 'authentication'),
    url(r'^SportSess/profil/$', 'profil'),
    url(r'^SportSess/friends/$', 'friends_list'),
    url(r'^SportSess/messages/$', 'messages'),
    url(r'^SportSess/sign_up/$', 'sign_up'),"""
)
