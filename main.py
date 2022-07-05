import os
import time
import sys
from app.client.api.client import *
from app.client.subMainInt import *
from app.local.subMainLocal import *

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
  time.sleep(1)
  while True:
    conexion = RestAPI()
    conectado = conexion.existsConnection()
    if conectado == False:
      print('\nConexion a internet no establecida...   ')
      time.sleep(2)
      print('\nVerifique su conexion a internet')
      time.sleep(2)
      print('\nLa informacion generada se almacenara localmente')
      op_l = operacionLocal()
      op_l.init_l()
      time.sleep(3)
      limpiar()
      print(titulo)
    else:
      try:
        print('\nConectado a internet   ')
        time.sleep(2)
        print('\nEjecutando operaciones')
        time.sleep(2)
        op_lo = operacionLocal()
        op_lo.locales()
        time.sleep(2)
        op_i = operacionInt()
        op_i.init_i()
      except KeyboardInterrupt:
        print('\n\nHasta pronto...')
        time.sleep(1)
        limpiar()
        break
except KeyboardInterrupt:
  print('\n\nHasta pronto...')
  time.sleep(1)
  limpiar()
  sys.exit(0)