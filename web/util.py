# -*- coding: utf-8 -*-

from django.template.defaultfilters import slugify;
from django.shortcuts import get_object_or_404;
from django.http import Http404;

from BlancoWeb.web.models import Redirect, Evento;

def slugifyUnico(value, model, slugfield='slug'):
        """Returns a slug on a name which is unique within a model's table

        This code suffers a race condition between when a unique
        slug is determined and when the object with that slug is saved.
        It's also not exactly database friendly if there is a high
        likelyhood of common slugs being attempted.

        A good usage pattern for this code would be to add a custom save()
        method to a model with a slug field along the lines of:

                from django.template.defaultfilters import slugify

                def save(self):
                    if not self.id:
                        # replace self.name with your prepopulate_from field
                        self.slug = SlugifyUniquely(self.name, self.__class__)
                super(self.__class__, self).save()

        Original pattern discussed at
        http://www.b-list.org/weblog/2006/11/02/django-tips-auto-populated-fields
        """
        suffix = 0
        potential = base = slugify(value)
        while True:
                if suffix:
                        potential = "-".join([base, str(suffix)])
                if not model.objects.filter(**{'slug': potential}).count():
                        return potential
                # we hit a conflicting slug, so bump the suffix & try again
                suffix += 1


class Http302(Exception):
    def __init__(self, redirect_to):
        self.redirect_to = redirect_to;

class Http301(Exception):
    def __init__(self, redirect_to):
        self.redirect_to = redirect_to;

def get_object_or_error(klass, *args, **kwargs):
    """
        Busca un objeto perteneciente al modelo klass
        en caso de no existir:
            si esta en la lista de Redirect, lanza excepcion 301 o 302
            si no esta, lanza excepcion 404
    """
    
    try:
        return get_object_or_404(klass, *args, **kwargs);
    except Http404:
        try:
            r = Redirect.objects.get(kwargs.popitem());
            if r.permanente:
                raise Http301(r.evento.get_absolute_url());
            else:
                raise Http302(r.evento.get_absolute_url());            
        except Redirect.DoesNotExist:
            raise Http404;
        
        
            
        