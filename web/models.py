from django.db import models;
from django.contrib.auth.models import User;
from django.contrib.sitemaps import ping_google;


from web.util import slugifyUnico;

# Create your models here.

class TipoEvento(models.Model):
    nombre = models.CharField(max_length=32);
    imagen = models.FileField(upload_to="eventos/", blank=True, null=True);
    
    def save(self, *args, **kwargs):
        
        super(TipoEvento, self).save();
        
            
    def __unicode__(self):
        return self.nombre;

class Evento(models.Model):
    nombre = models.CharField(max_length=128, blank=False);
    tipo_evento = models.ForeignKey(TipoEvento, blank=False);
    fecha = models.DateField(blank=False);
    hora_inicio = models.TimeField(blank=False);
    hora_fin = models.TimeField(blank=True, null=True);
    info = models.TextField(blank=False);
    creado = models.DateTimeField(auto_now_add=True, blank=False);
    autor = models.ForeignKey(User, editable=False);
    slug = models.SlugField(unique=True);
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugifyUnico(self.nombre, model=self.__class__);
        super(Evento, self).save();  
        try:
             ping_google();
        except Exception:
             # Bare 'except' because we could get a variety
             # of HTTP-related exceptions.
             pass;
         
    @models.permalink
    def get_absolute_url(self):
        return ('web.evento', [self.slug ]);
    
class Horario(models.Model):
    dias = models.CharField(max_length=128, blank=False);
    abierto = models.TimeField(blank=False);
    cerrado = models.TimeField(blank=False);
    
    def save(self, *args, **kwargs):
        super(Horario, self).save();
        
class Bienvenida(models.Model):
    texto = models.TextField(blank=False);
    imagen = models.FileField(upload_to="bienvenidas/", blank=True, null=True);
    
class Noticia(models.Model):
    titular = models.CharField(max_length=128, blank=True);
    cuerpo = models.TextField(blank=False);
    creado = models.DateTimeField(auto_now_add=True, blank=False); 
    autor = models.ForeignKey(User, editable=False);  
         
class Patrocinador(models.Model):
    imagen = models.FileField(upload_to="patrocinadores/", blank=True, null=True);
    nombre = models.CharField(max_length=128, blank=False);
    enlace = models.URLField(verify_exists=True, blank=False);
    
