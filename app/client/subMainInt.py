from .scripts.sensors import *
from .scripts.dataSensors import *
from datetime import datetime
import time
import os

class operacionInt:

    def init(self):
        self.sensores()
        self.archivos('TH', 'th/store')
        self.archivos('US', 'us/store')
        self.archivos('PIR', 'pir/store')
        self.archivos('GH', 'gh/store')
        print('\nEjecutando operacion de envio de datos')
        self.envio()

    def sensores(self):
        js = claseJson('sensores')
        sen = sensors()
        existe = js.existeJson()
        if existe == True:
            if sen.listaSensors == []:
                sen.cargarListaSensores()
                print('\nLista cargada')
            else:
                pass
        else:
            lista = sen.peticionSensores()
            sen.listarSensores(lista)
            dic = sen.diccionarioSensores()
            print('\n{}'.format(sen.guardarSensores(dic)))
    
    def archivos(self, file, path):
        js = claseJson(file)
        existe = js.existeJson()
        if existe == True:
            data = js.obtenerJson()
            api = RestAPI()
            api.endpoint = 'http://192.168.1.76:3333/'
            info = api.methodPost(path, data)
            print(info['mensaje'])
        else:
            print('\nEl archivo {} no existe'.format(file))

    def envio(self):
        while True:
            sen = sensors()
            sensores = sen.getSensors()
            for i in sensores:
                self.medicion(i)
                time.sleep(1)
    
    def medicion(self, sensor):
        if sensor.tipo == 'TH':
            sth = self.dataTH(sensor)
            print('\n{}'.format(sth))
        elif sensor.tipo == 'US':
            sus = self.dataUS(sensor)
            print('\n{}'.format(sus))
        elif sensor.tipo == 'PIR':
            spir = self.dataPIR(sensor)
            print('\n{}'.format(spir))
        elif sensor.tipo == 'GH':
            sgh = self.dataGH(sensor)
            print('\n{}'.format(sgh))
    
    def dataEstandarizada(self, sensorID, valores):
        tiempo = datetime.now()
        return {
            "sensorID": sensorID,
            "valores": valores,
            "fecha":tiempo.strftime('%d-%m-%Y'),
            "hora":tiempo.strftime('%I:%M')
        }

    def dataTH(self, sensor):
        api = RestAPI()
        api.endpoint = 'http://192.168.1.76:3333/'
        ds = dataSensors()
        pin = sensor.pines[0]
        sensorID = sensor._id
        arrayTH = ds.th(pin)
        valores = [{"temperatura":float(arrayTH[0])}, {"humedad":float(arrayTH[1])}]
        data = self.dataEstandarizada(sensorID, valores)
        mensaje = api.methodPost('th/store', data)
        return mensaje
        
    def dataUS(self, sensor):
        api = RestAPI()
        api.endpoint = 'http://192.168.1.76:3333/'
        ds = dataSensors()
        pin1 = sensor.pines[0]
        pin2 = sensor.pines[1]
        sensorID = sensor._id
        distancia = ds.us(pin1, pin2)
        valores = [{"distancia":distancia}]
        data = self.dataEstandarizada(sensorID, valores)
        mensaje = api.methodPost('us/store', data)
        return mensaje

    def dataPIR(self, sensor):
        api = RestAPI()
        api.endpoint = 'http://192.168.1.76:3333/'
        ds = dataSensors()
        pin = sensor.pines[0]
        sensorID = sensor._id
        presencia = ds.pir(pin)
        valores = [{"presencia": presencia}]
        data = self.dataEstandarizada(sensorID, valores)
        mensaje = api.methodPost('pir/store', data)
        return mensaje
    
    def dataGH(self, sensor):
        api = RestAPI()
        api.endpoint = 'http://192.168.1.76:3333/'
        ds = dataSensors()
        pin1 = sensor.pines[0]
        pin2 = sensor.pines[1]
        sensorID = sensor._id
        goh = ds.gh(pin1, pin2)
        valores = [{"gas o humo": goh}]
        data = self.dataEstandarizada(sensorID, valores)
        mensaje = api.methodPost('gh/store', data)
        return mensaje
        
            









