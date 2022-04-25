#!/usr/bin/python3

import os, sys

#OPCIONAL
#Este archivo se coloca en la ruta /usr/bin/
#Dale todos los privilegios al archivo
#Al escribir sensorbox.py se ejecutara el programa
#En caso de tener una zsh crearas un alias en el archivo .zshrc
#Ejemplo: alias sensorbox='sensorbox.py'
#Escribes sensorbox y ejecutara el programas

if len(sys.argv) != 1:
    print('\nUso: sensorbox | sensorbox.py ')
    sys.exit(0)
else:
    os.system('python3 /home/pi/sensorbox/main.py')