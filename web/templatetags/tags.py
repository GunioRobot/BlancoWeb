from django.template import Library, Node
from django.db.models import get_model
from datetime import datetime


register = Library()

class LatestNode(Node):
    def __init__(self, model, num, varname):
        self.num = num;
        self.varname = varname;
        self.model = get_model(*model.split('.'));
        
    def render(self, context):
        if self.num != -1:
            context[self.varname] = self.model.objects.all().order_by('-pk')[:self.num];
        else:
            context[self.varname] = self.model.objects.all();
        return '';
    
class NextNode(Node):
    def __init__(self, model, varname):
        self.model = get_model(*model.split('.'));
        self.varname = varname;
        
    def render(self, context):
        context[self.varname] = self.model.objects.filter(fecha__gte=datetime.now());
        return '';
    
class IdNode(Node):
    def __init__(self, model, id, varname):
        self.model = get_model(*model.split('.'));
        self.varname = varname;
        self.id = int(id);
        
    def render(self, context):
        context[self.varname] = self.model.objects.get(pk=self.id);
        return '';
    
class LastNode(Node):
    def __init__(self, model, id, varname):
        self.model = get_model(*model.split('.'));
        self.varname = varname;
        self.id = id;
        
    def render(self, context):
        context[self.varname] = self.model.objects.order_by(self.id)[0];
        return '';
    
def get_latest(parser, token):
    partes = token.contents.split();
    if len(partes) != 5:
        raise TemplateSyntaxError, "get_latest necesita 4 argumentos";
    if partes[3] != 'as':
        raise TemplateSyntaxError, "tercer argumento debe ser as";
    return LatestNode(model=partes[1], num=partes[2], varname=partes[4]);
get_latest = register.tag(get_latest)


def get_all(parser, token):
    partes = token.contents.split();
    if len(partes) != 4:
        raise TemplateSyntaxError, "get_all necesita 3 argumentos";
    elif partes[2] != 'as':
        raise TemplateSyntaxError, "segundo argumento debe ser as";
    
    return LatestNode(model=partes[1], num=-1, varname=partes[3]);
get_all = register.tag(get_all)

def get_next(parser, token):
    partes = token.contents.split();
    if len(partes) != 4:
       raise TemplateSyntaxError, "get_next necesita 3 argumentos";
    elif partes[2] != 'as':
        raise TemplateSyntaxError, "segundo argumento debe ser as";
    
    return NextNode(model=partes[1], varname=partes[3]);
get_next = register.tag(get_next)

def get_id(parser, token):
    partes = token.contents.split();
    if len(partes) != 5:
       raise TemplateSyntaxError, "get_id necesita 3 argumentos";
    elif partes[3] != 'as':
        raise TemplateSyntaxError, "segundo argumento debe ser as";
    
    return IdNode(model=partes[1], id=partes[2], varname=partes[4]);
get_id = register.tag(get_id)

def get_last(parser, token):
    partes = token.contents.split();
    if len(partes) != 5:
       raise TemplateSyntaxError, "get_last necesita 3 argumentos";
    elif partes[3] != 'as':
        raise TemplateSyntaxError, "segundo argumento debe ser as";
    
    return LastNode(model=partes[1], id=partes[2], varname=partes[4]);
get_last = register.tag(get_last)
    
                   