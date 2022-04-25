from ..scripts.sensors import *
from ..scripts.dataSensors import *
from datetime import datetime
import time

class operacionInt:

    def init_i(self):
        self.Sensores()
        print('\nEspere mientras se configura la conexion')
        time.sleep(10)
        self.nuevosSensores()
        self.archivos('TH', 'th/store')
        self.archivos('US', 'us/store')
        self.archivos('PIR', 'pir/store')
        self.archivos('GH', 'gh/store')
        print('\nEjecutando operacion de envio de datos')
        self.envio()

    def Sensores(self):
        js = claseJson('sensores')
        sen = sensors()
        sensores = sen.getSensors()
        existeSensores = js.existeJson()
        if existeSensores == True:
            if sensores == []:
                sen.cargarListaSensores('sensores', sensores)
                print('\nLista cargada')
        else:
            data = sen.peticionSensores()
            sen.listarSensores(data, sensores)
            dic = sen.diccionarioSensores(sensores)
            print('\n{}'.format(sen.guardarSensores(dic, 'sensores')))
    
    def nuevosSensores(self):
        #<>
        sen = sensors()
        sensores = sen.getNewSensors()
        data = sen.peticionSensores()
        sen.listarSensores(data, sensores)
        newSensores = sen.getNewSensors()
        oldSensores = sen.getSensors()
        if len(newSensores) > len(oldSensores):
            print('\nSe agrego un nuevo sensor')
            time.sleep(1)
            print('\nCargando de nuevo la lista')
            time.sleep(1)
            dic = sen.diccionarioSensores(newSensores)
            print(sen.guardarSensores(dic, 'sensores'))
            newSensores.clear()
            oldSensores.clear()
            sen.newlistaSensors.clear()
            sen.listaSensors.clear()
            sen.cargarListaSensores('sensores', sen.listaSensors)
            time.sleep(1)
            print('\nLista nuevamente cargada')
        else:
            print('\nNo se han agregado sensores')
            newSensores.clear()
            sen.newlistaSensors.clear()
    
    def archivos(self, file, path):
        js = claseJson(file)
        existe = js.existeJson()
        if existe == True:
            data = js.obtenerJson()
            if data == []:
                print('\nNo hay nada')
            else:
                api = RestAPI()
                api.endpoint = 'http://192.168.1.76:3333/'
                for x in data:
                    print(x)
                #info = api.methodPost(path, data)
                #print(info['mensaje'])
        else:
            print('\nEl archivo {} no existe'.format(file))

    def envio(self):
        while True:
            sen = sensors()
            sensores = sen.getSensors()
            for i in sensores:
                self.medicionInt(i)
    
    def medicionInt(self, sensor):
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
        else:
            sth = self.dataTH(sensor)
            print('\n{}'.format(sth))
    
    def dataEstandarizada(self, sensorID, valores):
        tiempo = datetime.now()
        return {
            "sensorID": sensorID,
            "valores": valores,
            "fecha":tiempo.strftime('%d-%m-%Y'),
            "hora":tiempo.strftime('%I:%M')
        }

    def dataTH(self, sensor):
        try:
            api = RestAPI()
            api.endpoint = 'http://192.168.1.76:3333/'
            ds = dataSensors()
            pin = sensor.pines[0]
            sensorID = sensor._id
            arrayTH = ds.th(pin)
            valores = [{"temperatura":arrayTH[0]}, {"humedad":arrayTH[1]}]
            data = self.dataEstandarizada(sensorID, valores)
            mensaje = api.methodPost('th/store', data)
            return mensaje['mensaje']
        except Exception as e:
            return 'Error en la conexion: {}'.format(e)
        
    def dataUS(self, sensor):
        try:
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
            return mensaje['mensaje']
        except Exception as e:
            return 'Error en la conexion: {}'.format(e)

    def dataPIR(self, sensor):
        try:
            api = RestAPI()
            api.endpoint = 'http://192.168.1.76:3333/'
            ds = dataSensors()
            pin = sensor.pines[0]
            sensorID = sensor._id
            presencia = ds.pir(pin)
            valores = [{"presencia": presencia}]
            data = self.dataEstandarizada(sensorID, valores)
            mensaje = api.methodPost('pir/store', data)
            return mensaje['mensaje']
        except Exception as e:
            return 'Error en la conexion: {}'.format(e)
    
    def dataGH(self, sensor):
        try:
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
            return mensaje['mensaje']
        except Exception as e:
            return 'Error en la conexion: {}'.format(e)
        
            









