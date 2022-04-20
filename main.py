import os
import time
import sys
from app.client.api.client import *

titulo = '''
         ____                            ____            
        / ___|  ___ _ __  ___  ___  _ __| __ )  _____  __
        \___ \ / _ \ '_ \/ __|/ _ \| '__|  _ \ / _ \ \/ /
         ___) |  __/ | | \__ \ (_) | |  | |_) | (_) >  < 
        |____/ \___|_| |_|___/\___/|_|  |____/ \___/_/\_\ 
                            
                                    
                            
                           FrellDevs341

'''

def limpiar():
    os.system('clear')

try:
    limpiar()
    print(titulo)
    print('\nPresione Ctrl + C para cancelar la operacion')
    time.sleep(2)
    print('\nComprobando conexion a internet...')
    conexion = RestAPI()
    conectado = conexion.existsConnection()
    time.sleep(2)
    while conectado == False:
        print('\nConexion a internet no establecida...   ')
        time.sleep(1)
        print('\nVerifique su conexion a internet')
        time.sleep(1)
        print('\nLa informacion generada se almacenara localmente')
        
        time.sleep(1)
        limpiar()
        print(titulo)
    else:
        print('\nConectado a internet   ')
        time.sleep(2)
        print('\nEjecutando operaciones')
        time.sleep(1)
        
    limpiar()
except KeyboardInterrupt:
    print('\n\nSaliendo...')
    time.sleep(1)
    os.system('clear')
    sys.exit(0)