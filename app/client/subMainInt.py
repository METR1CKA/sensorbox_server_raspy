from .scripts.sensors import *
from .scripts.dataSensors import *
from datetime import datetime
import time

class operacionInt:

    def init(self):
        self.sensores()
        #self.medicion()

    def sensores(self):
        js = claseJson('sensores')
        sen = sensors()
        existe = js.existeJson()
        if existe == True:
            if sen.listaSensors == []:
                sen.cargarListaSensores()
            else:
                pass
        else:
            lista = sen.peticionSensores()
            sen.listarSensores(lista)
            dic = sen.diccionarioSensores()
            print('\n{}'.format(sen.guardarSensores(dic)))
    
    def TH_E(self):
        js = claseJson('th_e')
        existe = js.existeJson()
        if existe == True:
            datos = js.obtenerJson()
            for x in datos:
                api = RestAPI()
                api.endpoint = 'http://192.168.1.76:3333/'
                valores = {
                    "sensorID":x['sensorID'],
                    "valores":[
                        {
                            "temperatura":x['valores']['temperatura']
                        },
                        {
                            "humedad":x['valores']['humedad']
                        }
                    ],
                    "fecha":x['fecha'],
                    "hora":x['hora']
                }
                print(api.methodPost('valores/data', valores))
                time.sleep(1)
    
    def GH(self):
        js = claseJson('th_e')
        existe = js.existeJson()
        if existe == True:
            pass
        else:
            pass
    
    def PIR(self):
        js = claseJson('th_e')
        existe = js.existeJson()
        if existe == True:
            pass
        else:
            pass

    def US(self):
        js = claseJson('th_e')
        existe = js.existeJson()
        if existe == True:
            pass
        else:
            pass

    def medicion(self):
        api = RestAPI()
        api.endpoint = 'http://192.168.1.76:3333/'
        sen = sensors()
        sensor = sen.getSensors()
        if sensor.tipo == 'TH_E':
            
            #sd = dataSensors()
            #valores = sd.thExterna(sensor)
            #datos = self.dictTH_E(sensor.ID, valores)
            #print('\n{}'.format(api.methodPost('valores/data',datos)))
            print(sensor.tipo)

    def pruebaTemperaturaHumedad(self):
        api = RestAPI()
        api.endpoint = 'http://192.168.1.76:3333/'
        ds = dataSensors()
        valores = ds.th()
        sensorID = 1
        data = self.dictTH(sensorID=sensorID, valores=valores)
        return data
        #resp = api.methodPost('th/store', data)
        #return resp



    def dictTH(self, sensorID=int(), valores=list()):
        tiempo = datetime.now()
        return {
            "sensorID": sensorID,
            "valores":[
                {
                    "temperatura":valores[1]
                },
                {
                    "humedad":valores[0]
                }
            ],
            "fecha":tiempo.strftime('%d-%m-%Y'),
            "hora":tiempo.strftime('%I:%M')
        }
        
            









