import json
import os.path
import os


class claseJson:

    def __init__(self, filename):
        self.filename = filename
        self.namefile = self.filename + ".json"
        self.namedir = "data/jsonDataSensors/"
        self.path_file = self.namedir + self.namefile

    def crearJson(self):
        try:
            if os.path.isfile(self.path_file):
                os.system('rm -rf {}'.format(self.path_file))
            else:
                os.system('touch {}'.format(self.path_file))
        except:
            return "No se creo el archivo"
    
    def llenarJson(self, listaDiccionario):
        try:
            if os.path.isfile(self.path_file):
                file = open(self.path_file, "w")
                file = json.dump(listaDiccionario, file)
                return 'Datos llenados correctamente'
            else:
                return 'El archivo no existe'
        except:
            return 'No se pudo crear el archivo'

    def obtenerJson(self):
        data = []
        if os.path.isfile(self.path_file):
            file = open(self.path_file, "r")
            data = json.loads(file.read())
        return data
    
    def existeJson(self):
        if os.path.isfile(self.path_file):
            return 'El archivo existe'
        else:
            return 'El archivo no existe'
