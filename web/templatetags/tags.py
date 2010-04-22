# -*- coding: utf-8 -*-

from django.template import Library, Node
from django.db.models import get_model
from datetime import datetime


register = Library()

"""
###########################
    DEFINICION DE LOS TIPOS DE NODO
###########################
""" 

class LatestNode(Node):
    def __init__(self, model, num, varname):
        self.num = num;
        self.varname = varname;
        self.model = get_model(*model.split('.'));
        
    def render(self, context):
        try:
            if self.num != -1:
                context[self.varname] = self.model.objects.all().order_by('-pk')[:self.num];
            else:
                context[self.varname] = self.model.objects.all();
        except:
            pass;
        return '';
    
class NextNode(Node):
    def __init__(self, model, varname):
        self.model = get_model(*model.split('.'));
        self.varname = varname;
        
    def render(self, context):
        try:
            context[self.varname] = self.model.objects.filter(fecha__gte=datetime.now());
        except:
            pass;
        return '';
    
class IdNode(Node):
    def __init__(self, model, id, varname):
        self.model = get_model(*model.split('.'));
        self.varname = varname;
        self.id = int(id);
        
    def render(self, context):
        try:
            context[self.varname] = self.model.objects.get(pk=self.id);
        except:
            pass;
        return '';
    
class LastNode(Node):
    def __init__(self, model, id, varname):
        self.model = get_model(*model.split('.'));
        self.varname = varname;
        self.id = id;
        
    def render(self, context):
        try:
            context[self.varname] = self.model.objects.order_by(self.id)[0];
        except:
            pass;
        return '';
 
"""
###########################
    FUNCIONES PARA OBTENER NODOS
###########################
"""   

def get_latest(parser, token):
    """
        Obtiene la lista con los ultimos elementos añadidos
        get_latest MODELO TAMAÑO as LISTA
    """
    partes = token.contents.split();
    if len(partes) != 5:
        raise TemplateSyntaxError, "get_latest necesita 4 argumentos";
    if partes[3] != 'as':
        raise TemplateSyntaxError, "tercer argumento debe ser as";
    return LatestNode(model=partes[1], num=partes[2], varname=partes[4]);
get_latest = register.tag(get_latest)


def get_all(parser, token):
    """
        Obtiene la lista con todos los elementos añadidos
        get_all MODELO as LISTA
    """
    partes = token.contents.split();
    if len(partes) != 4:
        raise TemplateSyntaxError, "get_all necesita 3 argumentos";
    elif partes[2] != 'as':
        raise TemplateSyntaxError, "segundo argumento debe ser as";
    
    return LatestNode(model=partes[1], num= -1, varname=partes[3]);
get_all = register.tag(get_all)

def get_next(parser, token):
    """
        Obtiene la lista con siguientes elementos añadidos con fecha futura
        get_latest MODELO as LISTA
    """
    partes = token.contents.split();
    if len(partes) != 4:
       raise TemplateSyntaxError, "get_next necesita 3 argumentos";
    elif partes[2] != 'as':
        raise TemplateSyntaxError, "segundo argumento debe ser as";
    
    return NextNode(model=partes[1], varname=partes[3]);
get_next = register.tag(get_next)

def get_id(parser, token):
    """
        Obtiene un objeto determinado por su id
        get_id MODELO ID as OBJETO
    """
    partes = token.contents.split();
    if len(partes) != 5:
       raise TemplateSyntaxError, "get_id necesita 4 argumentos";
    elif partes[3] != 'as':
        raise TemplateSyntaxError, "tercer argumento debe ser as";
    
    return IdNode(model=partes[1], id=partes[2], varname=partes[4]);
get_id = register.tag(get_id)

def get_last(parser, token):
    """
        Obtiene el ultimo objeto añadido ordenado por ORDEN
        get_last MODELO ORDEN as OBJETO
    """
    partes = token.contents.split();
    if len(partes) != 5:
       raise TemplateSyntaxError, "get_last necesita 4 argumentos";
    elif partes[3] != 'as':
        raise TemplateSyntaxError, "tercer argumento debe ser as";
    
    return LastNode(model=partes[1], id=partes[2], varname=partes[4]);
get_last = register.tag(get_last)
    
                   
