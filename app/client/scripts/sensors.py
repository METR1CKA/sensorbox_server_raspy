from ..api.client import *
from ...local.data.dataJson import claseJson

class sensors:

    listaSensors = []

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

    def __init__(self, listaSensors=list()):
        self.listaSensors = listaSensors
    
    def peticionSensores(self):
        api = RestAPI()
        api.endpoint = 'http://192.168.1.76:3333/'
        datos = api.methodGet('sensors')
        sensores = datos['data']
        return sensores
    
    def getSensors(self):
        return self.listaSensors

    def listarSensores(self, data):
        for i in data:
            sen = sensors()
            sen._id = i['_id']
            sen.nombre = i['nombre']
            sen.pines = i['pin']
            sen.tipo = i['tipo']
            self.listaSensors.append(sen)

    def sensoresDiccionario(self):
        return {
            "ID":self._id,
            "Nombre":self.nombre,
            "Pines": self.pines,
            "Tipo":self.tipo
        }

    def diccionarioSensores(self):
        ld = []
        for i in self.listaSensors:
            ld.append(i.sensoresDiccionario())
        return ld
    
    def guardarSensores(self, ld):
        js = claseJson('sensores')
        js.crearJson()
        msg = js.llenarJson(ld)
        return msg

    def cargarListaSensores(self):
        js = claseJson('sensores')
        data = js.obtenerJson()
        for i in data:
            sen = sensors()
            sen._id = i['ID']
            sen.nombre = i['Nombre']
            sen.pines = i['Pines']
            sen.tipo = i['Tipo']
            self.listaSensors.append(sen)
    
    
        
