from blanco.web.models import *;
from django.contrib import admin;

'''
    Tipos de evento
'''

class EventoAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'fecha', 'tipo_evento',);
    exclude = ('slug',);
    
    def save_model(self, request, obj, form, change):
        obj.autor = request.user;
        obj.save();
        
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('dias', 'abierto', 'cerrado',);
    
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titular', 'cuerpo', 'creado'); 
    
    def save_model(self, request, obj, form, change):
        obj.autor = request.user;
        obj.save();
        
class PatrocinadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'enlace');
    
class BienvenidaAdmin(admin.ModelAdmin):
    list_display = ('texto', 'imagen');

admin.site.register(Evento, EventoAdmin);
admin.site.register(TipoEvento);
admin.site.register(Horario, HorarioAdmin);
admin.site.register(Bienvenida, BienvenidaAdmin);
admin.site.register(Noticia, NoticiaAdmin);
admin.site.register(Patrocinador, PatrocinadorAdmin);
