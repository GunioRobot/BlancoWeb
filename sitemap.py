from django.contrib.sitemaps import Sitemap;
from web.models import Evento, Noticia;

class EventoSitemap(Sitemap):
    changefrep = "never";
    priority = 0.5;
    
    def items(self):
        return Evento.objects.all();
    
    def lastmod(self, obj):
        return obj.creado;
    
class NoticiaSitemap(Sitemap):
    changefrep = "never";
    priority = 0.4;
    
    def items(self):
        return Noticia.objects.all();
    
    def lastmod(self, obj):
        return obj.creado;

