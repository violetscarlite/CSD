from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
import csd_site.settings
from csd_site.settings import MEDIA_ROOT, STATIC_ROOT

loginPatterns = patterns('', 
	url(r'^login/$','csd_app.views.authLogin'),
	url(r'^login/successful$','csd_app.views.loginSuccess'),
	url(r'^logout/$','csd_app.views.logoutUser'),
)

urlpatterns = patterns('',
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}), 

    url(r'^home$', 'csd_app.views.home'),
    url(r'^$', 'csd_app.views.home'),
    url(r'^setup/create$', 'csd_app.views.createSetup'),
    url(r'^setup/manage$', 'csd_app.views.manageSetups'),

    url(r'^',include(loginPatterns)),
)

