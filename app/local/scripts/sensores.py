from app.client.api.client import RestAPI

class sensors:

    listaSensors = []

    def __init__(self, _id, nombre, pin, tipo):
        self._id = _id
        self.nombre = nombre
        self.pin = pin
        self.tipo = tipo

    def __init__(self):
        self._id = 0
        self.nombre = ''
        self.pin = []
        self.tipo = ''
    
    def sensorsDicc(self):
        return {
            "ID": self._id,
            "Nombre": self.nombre,
            "Pin": self.pin,
            "Tipo": self.tipo
        }
    
    def listarDiccionario(self):
        ld = []
        for i in self.listaSensors:
            ld.append(i.sensorsDicc())
        return ld
    
    def jsonToObject(self, filename):
        js = claseJson(filename=filename)
        data = js.obtenerJson()
        for i in data:
            s = sensors()
            s._id = i["ID"]
            s.nombre = i["Nombre"]
            s.pin.append(i["Pin"])
            s.tipo = i["Tipo"]
            self.listaSensors.append(s)