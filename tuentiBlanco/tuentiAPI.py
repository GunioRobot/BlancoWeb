# -*- coding: utf-8 -*-

import httplib, urllib;
from django.utils import simplejson;
from django.http import HttpResponse;
from settings import TUENTI_MAIL, TUENTI_PASS;

class TuentiError(Exception):
    def __init__(self, cod=0, msg=''):
        self.cod = cod;
        self.msg = msg;
        
    def __str__(self):
        return str(self.cod) + ' ' + self.msg;



class TuentiAPI:
    
    def __init__(self, email, password):
        '''
            Constructor 
            Inicializa la conexion con el servidor de tuenti
            obteniendo el sessionID
        '''
        
        self.__email = email;
        self.__password = password;
        #primero hacemos el getChallenge
        json = __getJSON('getChallenge', {'type' : 'login'});
        response = self.__http(json); 
        print response;
    
    def __getJSON(self, method, param):
        '''
            añade toda la informacion necesaria
            para enviar en la request a tuenti
        '''
        implejson.dumps(['getChallenge', {'type' : 'login'}]);
        
    def __http(self, header):
        '''
            Realiza la peticion HTTP al servidor
            @return respuesta http
            @raise error 404 si falla
        '''
        #parametros a pasar (incluye operacion, etc)
        ##params = urllib.urlencode(json);
        
        #headers = ['Content-Length', json];
        print header;
        #conectar con el servidor
        conn = httplib.HTTPConnection('api.tuenti.com');
        response = conn.request('POST', '/api', header);
        response = conn.getresponse();
        
        if response.status == 200:
           data = response.read();
           conn.close();
           #return HttpResponse(data);
           return data
        print response.msg;
        conn.close();
        raise TuentiError(response.status, response.reason);

try:
    conectar = TuentiAPI(TUENTI_MAIL, TUENTI_PASS);
except TuentiError, e:
    print e;
