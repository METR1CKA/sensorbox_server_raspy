import pymongo


class conexionMongo:

    def __init__(self, col):
        mongoURI = 'mongodb://13.56.169.53:27017/test?compressors=disabled&gssapiServiceName=mongodb'
        self.myclient = pymongo.MongoClient(mongoURI)
        self.mydb = self.myclient['sensorbox']
        self.mycol = self.mydb[col]

    def crearUno(self, diccionario):
        self.mycol.insert_one(diccionario)
        return 'Guardado con exito'

    def crearMuchos(self, arrayDic):
        self.mycol.insert_many(arrayDic)
        return 'Datos guardados con exito'
