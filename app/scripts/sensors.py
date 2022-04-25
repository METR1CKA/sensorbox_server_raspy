from ..client.api.client import *
from ..local.data.dataJson import *

class sensors:

    listaSensors = []
    newlistaSensors = []

    def __init__(self, _id, nombre, pines, tipo):
        self._id = _id
        self.nombre = nombre
        self.pines = pines
        self.tipo = tipo

    def __init__(self):
        self._id = 0
        self.nombre = ''
        self.pines = []
        self.tipo = ''

    def __init__(self, listaSensors=list(), newlistaSensors=list()):
        self.listaSensors = listaSensors
        self.newlistaSensors = newlistaSensors
    
    def peticionSensores(self):
        api = RestAPI()
        api.endpoint = 'http://192.168.1.76:3333/'
        datos = api.methodGet('sensors/get')
        sensores = datos['data']
        return sensores
    
    def getSensors(self):
        return self.listaSensors
    
    def getNewSensors(self):
        return self.newlistaSensors

    def listarSensores(self, data, lista):
        for i in data:
            sen = sensors()
            sen._id = i['_id']
            sen.nombre = i['nombre']
            sen.pines = i['pin']
            sen.tipo = i['tipo']
            lista.append(sen)

    def sensoresDiccionario(self):
        return {
            "ID":self._id,
            "Nombre":self.nombre,
            "Pines": self.pines,
            "Tipo":self.tipo
        }

    def diccionarioSensores(self, lista):
        ld = []
        for i in lista:
            ld.append(i.sensoresDiccionario())
        return ld
    
    def guardarSensores(self, data, file):
        js = claseJson(file)
        js.crearJson()
        msg = js.llenarJson(data)
        return msg

    def cargarListaSensores(self, file, lista):
        js = claseJson(file)
        data = js.obtenerJson()
        for i in data:
            sen = sensors()
            sen._id = i['ID']
            sen.nombre = i['Nombre']
            sen.pines = i['Pines']
            sen.tipo = i['Tipo']
            lista.append(sen)
    
    
        
