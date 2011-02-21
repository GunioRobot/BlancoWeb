# -*- coding: utf-8 -*-
from django.contrib.syndication.feeds import Feed;
from web.models import Evento;

class EventoFeed(Feed):
    title = "Blanco Irish Tavern";
    link = "web/feeds/eventos/";
    description = "Suscríbete para conocer todas nuestras fiestas"
    
    def items(self):
        return Evento.objects.all().order_by("-fecha");
    
    def item_title(self, item):
        return item.nombre
    
    def item_description(self, item):
        descripcion = "%s" % item.fecha;
        descripcion += " %s" % item.hora_inicio;
        descripcion += " %s" % item.info;
        return descripcion;