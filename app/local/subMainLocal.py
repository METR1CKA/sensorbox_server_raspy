from app.client.subMainInt import *
from ..scripts.dataSensors import *
from ..scripts.sensors import *

class operacionLocal:

  listaTH = []
  listaUS = []
  listaPIR = []
  listaGH = []
  listaNueva = []

  def __init__(self):
    self.listaTH = []
    self.listaUS = []
    self.listaPIR = []
    self.listaGH = []
    self.listaNueva = []

  def __init__(self, listaNueva=list(),listaTH=list(), listaUS=list(), listaPIR=list(), listaGH=list()):
    self.listaTH = listaTH
    self.listaUS = listaUS
    self.listaPIR = listaPIR
    self.listaGH = listaGH
    self.listaNueva = listaNueva

  def init_l(self):
    self.SensoresLocal()
    self.guardarData()

  def SensoresLocal(self):
    js = claseJson('sensores')
    sen = sensors()
    sensores = sen.getSensors()
    existeSensores = js.existeJson()
    if existeSensores == True:
      if sensores == []:
        sen.cargarListaSensores('sensores', sensores)
        print('\nLista cargada')
    else:
      print('\nEl archivo no existe')

  def guardarData(self):
    sen = sensors()
    sensores = sen.getSensors()
    for i in sensores:
      self.medicionLocal(i)

  def medicionLocal(self, sensor):
    if sensor.tipo == 'TH':
      lista = self.getTH()
      sth = self.guardarTH(sensor, lista)
      print('\n{}'.format(sth))
    elif sensor.tipo == 'US':
      sus = self.guardarUS(sensor)
      print('\n{}'.format(sus))
    elif sensor.tipo == 'PIR':
      spir = self.guardarPIR(sensor)
      print('\n{}'.format(spir))
    elif sensor.tipo == 'GH':
      sgh = self.guardarGH(sensor)
      print('\n{}'.format(sgh))
    else:
      lista = self.getNewList()
      sth = self.guardarTH(sensor, lista)
      print('\n{}'.format(sth))

  def guardarTH(self, sensor, lista):
    try:
      ds = dataSensors()
      o = operacionInt()
      pin = sensor.pines[0]
      sensorID = sensor._id
      arrayTH = ds.th(pin)
      valores = [{"temperatura":arrayTH[0]}, {"humedad":arrayTH[1]}]
      data = o.dataEstandarizada(sensorID, valores)
      lista.append(data)
      return 'Datos de {} guardados'.format(sensor.nombre)
    except Exception as e:
      return 'Error {}'.format(e)

  def guardarUS(self, sensor):
    try:
      ds = dataSensors()
      pin1 = sensor.pines[0]
      pin2 = sensor.pines[1]
      sensorID = sensor._id
      ds = dataSensors()
      pin1 = sensor.pines[0]
      pin2 = sensor.pines[1]
      sensorID = sensor._id
      distancia = ds.us(pin1, pin2)
      valores = [{"distancia":distancia}]
      o = operacionInt()
      data = o.dataEstandarizada(sensorID, valores)
      self.listaUS.append(data)
      return 'Datos de {} guardados'.format(sensor.nombre)
    except Exception as e:
      return 'Error {}'.format(e)

  def guardarPIR(self, sensor):
    try:
      o = operacionInt()
      ds = dataSensors()
      pin = sensor.pines[0]
      sensorID = sensor._id
      presencia = ds.pir(pin)
      valores = [{"presencia": presencia}]
      data = o.dataEstandarizada(sensorID, valores)
      self.listaPIR.append(data)
      return 'Datos de {} guardados'.format(sensor.nombre)
    except Exception as e:
      return 'Error {}'.format(e)

  def guardarGH(self, sensor):
    try:
      o = operacionInt()
      ds = dataSensors()
      pin1 = sensor.pines[0]
      pin2 = sensor.pines[1]
      sensorID = sensor._id
      goh = ds.gh(pin1, pin2)
      valores = [{"gas o humo": goh}]
      data = o.dataEstandarizada(sensorID, valores)
      self.listaGH.append(data)
      return 'Datos de {} guardados'.format(sensor.nombre)
    except Exception as e:
      return 'Error {}'.format(e)

  def archivoJson(self, data, file):
    js = claseJson(file)
    js.crearJson()
    msg = js.llenarJson(data)
    return msg

  def getTH(self):
    return self.listaTH

  def getUS(self):
    return self.listaUS

  def getPIR(self):
    return self.listaPIR

  def getGH(self):
    return self.listaGH

  def getNewList(self):
    return self.listaNueva

  def locales(self):
    local = operacionLocal()
    myTH = local.getTH()
    myUS = local.getUS()
    myPIR = local.getPIR()
    myGH = local.getGH()
    newList = local.getNewList()
    self.archivoJson(myTH, 'TH')
    self.archivoJson(myUS, 'US')
    self.archivoJson(myPIR, 'PIR')
    self.archivoJson(myGH, 'GH')
    self.archivoJson(newList, 'Nuevo')
