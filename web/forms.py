from django import forms;
from django.forms import ModelForm, widgets;
from web.models import *;

class EventoForm(ModelForm):
    tipo = forms.ModelChoiceField(TipoEvento.objects, required=False);
    class Meta:
        model = Evento;
        exclude = ('autor', 'tipo_evento',)

        
class TipoEventoForm(ModelForm):
    class Meta:
        model = TipoEvento;

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100);
    email = forms.EmailField();
    mensaje = forms.CharField(widget=forms.Textarea);

    
