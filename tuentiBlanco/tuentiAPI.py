# -*- coding: utf-8 -*-

from httplib import HTTPConnection;
from django.utils import simplejson;
from hashlib import md5;
from settings import TUENTI_MAIL, TUENTI_PASS;

class TuentiError(Exception):
    """
        Clase excepcion para conectar con tuenti
    """
    def __init__(self, cod=0, msg=''):
        self.cod = cod;
        self.msg = msg;
        
    def __str__(self):
        return "EXCEPCION: " + str(self.cod) + ' ' + self.msg;

class TuentiAPI:
    """
        Clase para realizar llamadas a la API publica de Tuenti
        Basada en el trabajo de scromega
        
        http://github.com/scromega/tuentiAPI
        http://scromega.net/7-accediendo-a-la-api-cerrada-de-tuenti.html
    """
    
    user_data = {};
    email = '';
    __url = 'api.tuenti.com';
    
    def __init__(self, email, password):
        """
            Constructor 
            Inicializa la conexion con el servidor de tuenti
            obteniendo todo el user_data si todo fue correcto
        """
        
        self.email = email;

        #primero hacemos el getChallenge
        json = self.__getJSON(method='getChallenge', param={'type' : 'login'});
        response = self.__http(json);
        response = simplejson.loads(response)[0];
        
        #encripta el password
        passE = self.__md5(response['challenge']+self.__md5(password));
        appkey = ('MDI3MDFmZjU4MGExNWM0YmEyYjA5MzRkODlm'+
                  'Mjg0MTU6MC4xMzk0ODYwMCAxMjYxMDYwNjk2');
              
        #identificarse
        json = self.__getJSON(method='getSession',param={
            "passcode":passE,
            "application_key":appkey,
            "timestamp":response['timestamp'],
            "seed":response['seed'],
            "email":self.email
        });
        
        response = self.__http(json);
        self.user_data = simplejson.loads(response)[0];
        
    
    def __getJSON(self, method, param):
        """
            añade toda la informacion necesaria
            para enviar en la request a tuenti
        """

        request = {}
        
        if self.user_data.get("session_id",False):
            request['session_id'] = self.user_data['session_id'];
        request['version'] = '0.4'
        request['requests'] = [[method, param]];
        
        return simplejson.dumps(request)
        
    def __http(self, data):
        """
            Realiza la peticion HTTP al servidor
            @return respuesta http
            @raise TuentiError si falla
        """
        headers = {"Content-length":str(len(data))}
        #conectar con el servidor
        
        conn = HTTPConnection(host=self.__url);
        response = conn.request('POST','api/' , headers=headers, body=data);
        response = conn.getresponse();
        
        if response.status == 200:
           data = response.read();
           conn.close();
           return data
        conn.close();
        raise TuentiError(response.status, response.reason);
    
    def __md5(self, data):
        """
            Encriptacion utilizando el algoritmo md5
        """
        return md5(data).hexdigest();
    
    def request(self, method, param):
        json = self.__getJSON(method, param);
        response = self.__http(json);
        return simplejson.loads(response)[0];
        
        

try:
    tuenti = TuentiAPI(TUENTI_MAIL, TUENTI_PASS);
    print tuenti.user_data;
    print tuenti.request("getInbox",{})
except TuentiError, e:
    print e;
