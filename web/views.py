from django.template import Context, RequestContext;
from django.shortcuts import render_to_response, get_object_or_404;
from django.http import Http404, HttpResponseRedirect;
from django.contrib.auth.decorators import login_required, permission_required;
from django.core.mail import mail_managers;
from django.core.urlresolvers import reverse;

from web.models import *;
from web.forms import EventoForm, ContactoForm;



def index(request, context_instance=None):
    '''
        Vista de la pagina principal
    '''
    c = RequestContext(request);
    
    return render_to_response('web/index.html',{}, context_instance=c);



def raise404(request, context_instance=None):
    
    raise Http404;

    
    
def evento(request, id, context_instance=None):
    '''
        Vista para los eventos
    '''
    
    c = RequestContext(request);
    
    if id.isdigit():
        evento = get_object_or_404(Evento, pk=id);
    else:
		evento = get_object_or_404(Evento, slug=id);
    
    return render_to_response('web/evento.html',{'info': evento,'tipo': evento.tipo_evento,}, context_instance=c);


def galeria(request, context_instance=None):
    
    return index(request, context_instance);
    

def contacto(request, context_instance=None):
    
    c = RequestContext(request);
 
    if request.method == 'POST':
        form = ContactoForm(request.POST, prefix='contacto_form');
        if form.is_valid():
            mensaje = "Nombre: " + form.cleaned_data['nombre'] + "\nDireccion: " + form.cleaned_data['email'] + " escribio:\n\n" + form.cleaned_data['mensaje'];
            mail_managers('Mensaje desde la web', mensaje, fail_silently=False);
            return render_to_response('web/contacto.html', {'enviado': True}, context_instance=c);
    else:
        form = ContactoForm(prefix='contacto_form');

    return render_to_response('web/contacto.html', {'form' : form}, context_instance=c);
