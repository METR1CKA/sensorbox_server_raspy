# SENSORBOX

FRELLDEVS

## Python

* SERVER RASPBERRY

## ¿Que es?
Sensorbox es una solucion para ambientes laborales comerciales, en este caso de carnicerias o lugares que requieren un cuarto frio.
Sensorbox esta pensado para ayudar al manejo de la informacion dentro de un cuarto frio, asi se administra y ayuda a que el producto no se heche a perder

## ¿Cual es el objetivo?
Que sensorbox sea una herramienta utilizada por todos y que brinde una solucion al cliente

## ¿De que trata?
El repositorio trata de mostrar el proyecto que se elaboro del lado del servidor.
El servidor es una raspberry que junto con python y las librerias GPIO, requests, entre otros, ayudan a la gestion de los sensores y su informacion
Este proyecto ira evolucionando y cambiando conforme pase el tiempo, añadiendo y quitando varias cosas de las versiones pasadas
El proyecto es open source o de codigo abierto para todo aquel que lo necesite o quiera aportar

## Recursos utilizados

* Python
* Raspberry pi 3 Model B+
* Requests
* GPIO

> Este sistema creado en python solo funciona en sistemas Linux raspberryOS

# Uso

1. Debera instalar con `pip` los recursos de *Requests* y de *GPIO*

2. Debera instalar las `NerdFonts` en su terminal para visualizar mejor el diseño de la interfaz del programa

## Opcional

### *Archivo sensorbox.py*

1. Este archivo se coloca en la ruta `/usr/bin/` de su sistema Linux

2. Darle todos los privilegios al archivo con `sudo chmod 777 sensorbox.py`

3. Cierre la terminal y vuelva a abrir una nueva

4. Al escribir `sensorbox.py` en su terminal, se ejecutara el programa

5. Puede escribir `sensorbox.py -h` para obtener información de uso

### *ZSH o BASH*

1. En tu sistema Linux raspberryOS, por defecto, el tipo de *SHELL* es una *BASH*, en caso de tener una *ZSH* en lugar de una *BASH*, crearas un alias en el archivo `~/.zshrc`

2. Ejemplo:
    * `alias sensorbox='sensorbox.py'`

3. Cierre la terminal y vuelva a abrir una nueva

4. Escribes sensorbox y de igual manera ejecutaras el programa

## Arbol de directorios

```console
sensorbox_server_raspy
├── app
│   ├── client
│   │   ├── api
│   │   │   └── client.py
│   │   └── subMainInt.py
│   ├── local
│   │   ├── data
│   │   │   ├── dataJson.py
│   │   │   └── jsonDataSensores
│   │   │       ├── GH.json
│   │   │       ├── Nuevo.json
│   │   │       ├── PIR.json
│   │   │       ├── sensores.json
│   │   │       ├── TH.json
│   │   │       └── US.json
│   │   └── subMainLocal.py
│   └── scripts
│       ├── dataSensors.py
│       └── sensors.py
├── main.py
├── README.md
└── sensorbox.py

7 directories, 15 files
```

# **METR1CKA**

> [Pagina web](https://metr1cka.github.io "Visitanos en DevBlogs")

> [Mas repositorios](https://github.com/METR1CKA "Mi perfil")
