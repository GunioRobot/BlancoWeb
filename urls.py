from django.conf.urls.defaults import *;
from blanco.web.models import Evento;
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap;
from blanco.sitemap import *;
from django.views.generic import list_detail;

# Uncomment the next two lines to enable the admin:
from django.contrib import admin;
admin.autodiscover()

sitemaps = {
    'flatpages': FlatPageSitemap,
    'eventos': EventoSitemap,
    'noticias': NoticiaSitemap,
}


urlpatterns = patterns('',
    # Example:
    #(r'^blanco/', include('blanco.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^admin/', include(admin.site.urls)),
    (r'^web/', include('blanco.web.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media/'}),
    (r'^$', 'django.views.generic.simple.redirect_to', {'url':'/web/'}),
)
