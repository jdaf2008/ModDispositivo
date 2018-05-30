# ModDispositivo
Este repositorio contiene el código relacionado con el modulo dispoitivo del proyecto de medición de variables contaminantes.  Divulgación  datos de sensores y recepción de solicitudes.Se uso Raspberry Pi como central principal y las lecturas se toman de un shield y un arduino (a través del puerto serial)

## Instrucciónes de instalación
### Cliente RESTFul

El cliente fue desarrollado en Python con el microframework Flask.

1. Instalar librerias: httplib2 y Flask, antes upgrade pip 
*pip install --upgrade pip
*sudo pip install httplib2
*sudo pip install Flask


2. Para verificar instalación de librerias
*pip list

3. Correr archivo
*python dispClient.py
 
### Lectura serial de doatos provenientes de arduino

El archivo se denomina readSensor.py y lee los datos de los sensores provenientes del puerto USB, comunicaci�n serial

1. Instalar libreria serial para python y python3
*python -m pip install pyserial
*python3 -m pip install pyserial
