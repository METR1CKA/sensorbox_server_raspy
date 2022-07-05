#!/usr/bin/python3

import os, sys

if len(sys.argv) != 1:
  print('\nUso: sensorbox | sensorbox.py ')
  sys.exit(0)
else:
  os.system('python3 /home/pi/sensorbox/main.py')