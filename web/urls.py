# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail;

from web.models import Evento;
from web.feeds import EventoFeed;

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

evento_info = {
    'queryset' : Evento.objects.all().order_by('-fecha'),
    'template_object_name' : 'eventos',
    'allow_empty': True,
    'paginate_by' : 30,

}

feeds = {
    'eventos': EventoFeed
}


urlpatterns = patterns('',
    (r'^donde/$', 'web.views.raise404', {}, 'web.donde'),
    (r'^contacto/$', 'web.views.contacto', {}, 'web.contacto'),
    #(r'^galeria/$', 'blanco.web.views.galeria', {}, 'web.galeria'),
    #(r'^admin/evento/nuevo/$', 'blanco.web.views.adminEventoNuevo', {}, 'web.admin.evento.nuevo'),
    #(r'^admin/evento/edit/(?P<id>[^/]*)/$', 'blanco.web.views.adminEventoEdit', {}, 'web.admin.evento.edit'),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}, 'web.feeds.eventos'),
    (r'^evento/(?P<id>[^/]*)/$', 'web.views.evento', {}, 'web.evento'),
    (r'^eventos/$', list_detail.object_list, evento_info, 'web.eventos'),
    (r'^$', 'web.views.index', {}, 'web.index'),
    # Example:
    # (r'^blanco/', include('blanco.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
)
