import json
import os.path
import os

class claseJson:

  def __init__(self, filename):
    self.filename = filename
    self.namefile = self.filename + ".json"
    self.namedir = "/home/pi/sensorbox/app/local/data/jsonDataSensores/"
    self.path_file = self.namedir + self.namefile

  def crearJson(self):
    if os.path.isfile(self.path_file):
      os.system('rm -rf {}'.format(self.path_file))
      os.system('touch {}'.format(self.path_file))
    else:
      os.system('touch {}'.format(self.path_file))

  def llenarJson(self, listaDiccionario):
    if os.path.isfile(self.path_file):
      file = open(self.path_file, "w")
      file = json.dump(listaDiccionario, file)
      return 'Datos llenados correctamente'
    else:
      return 'El archivo no existe'

  def obtenerJson(self):
    data = []
    if os.path.isfile(self.path_file):
      file = open(self.path_file, "r")
      data = json.loads(file.read())
    return data

  def existeJson(self):
    if os.path.isfile(self.path_file):
      return True
    else:
      return False
