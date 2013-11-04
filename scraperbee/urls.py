from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from api.api import EntryResource

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

entry_resource = EntryResource()

urlpatterns = patterns('',
    (r'^entry/', include(entry_resource.urls)),

    # Examples:
    # url(r'^$', 'scraperbee.views.home', name='home'),
    # url(r'^scraperbee/', include('scraperbee.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
