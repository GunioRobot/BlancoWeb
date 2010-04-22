# -*- coding: utf-8 -*-

from django.template import Context, RequestContext;
from django.shortcuts import render_to_response, get_object_or_404;
from django.http import Http404, HttpResponseRedirect, HttpResponsePermanentRedirect;
from django.contrib.auth.decorators import login_required, permission_required;
from django.core.mail import mail_managers;
from django.core.urlresolvers import reverse;

from web.models import *;
from web.forms import EventoForm, ContactoForm;
from web.util import get_object_or_error, Http301, Http302;



def index(request, context_instance=None):
    """
        Vista de la pagina principal
    """
    c = RequestContext(request);
    
    return render_to_response('web/index.html', {}, context_instance=c);



def raise404(request, context_instance=None):
    """
        Las flatpages se buscan al saltar un 404
    """
    
    raise Http404;

    
    
def evento(request, id, context_instance=None):
    """
        Vista para los eventos
    """
    
    c = RequestContext(request);
    
    if id.isdigit():
        evento = get_object_or_404(Evento, pk=id);
    else:
        try:
		          evento = get_object_or_error(Evento, slug=id);
        except Http301, (e):
            return HttpResponsePermanentRedirect(e.redirect_to);
        except Http302, (e):
            return HttpResponseRedirect(e.redirect_to);
    
    return render_to_response('web/evento.html', {'info': evento, 'tipo': evento.tipo_evento, }, context_instance=c);


def galeria(request, context_instance=None):
    
    return index(request, context_instance);
    

def contacto(request, context_instance=None):
    """
        formulario con el contacto y envio de correos
    """
    
    c = RequestContext(request);
 
    if request.method == 'POST':
        form = ContactoForm(request.POST, prefix='contacto_form');
        if form.is_valid():
            mensaje = "Nombre: " + form.cleaned_data['nombre'] + "\nDireccion: " + form.cleaned_data['email'] + " escribió:\n\n" + form.cleaned_data['mensaje'];
            mail_managers('Mensaje desde la web', mensaje, fail_silently=False);
            return render_to_response('web/contacto.html', {'enviado': True}, context_instance=c);
    else:
        form = ContactoForm(prefix='contacto_form');

    return render_to_response('web/contacto.html', {'form' : form}, context_instance=c);
