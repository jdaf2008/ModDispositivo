#!/usr/bin/python3

# Funcion para el envio de variables de factores contaminantes al proyecto SIMONA
# Version 2.0
# Creado por Juan David Arias jdariasf@correo.udistrital.edu.co 31 de mayo de 2018

import httplib2
import json
import time
import datetime
from pprint import pprint
from Sensor import Sensor
from readSensor import getNoise, getAirQ, getMetano
import interrupt_client, MCP342X, wind_direction, HTU21D, bmp085, tgs2600, ds18b20_therm

URL_BASE = "http://ec2-54-202-254-90.us-west-2.compute.amazonaws.com:8080/"
URL_API = "/backendAmbiente/webresources/generic/"
URL_NAME_METHOD = "saveMedicion"
# dirJSON = "./ModDispositivo/clienteServer/testSensores.JSON"
dirJSON = "testSensores.JSON"

def getSensorData():

        presion = Sensor("1","presion",bmp085.BMP085().get_pressure(),True)
        temp = Sensor("2","temperatura", ds18b20_therm.DS18B20().read_temp(),True)
        air = Sensor("3","calidadAire",tgs2600.TGS2600(adc_channel = 0).get_value(),True)
        humidity = Sensor("4","humedad",HTU21D.HTU21D().read_temperature(),True)
        metano = Sensor("5", "metano",getMetano(),True)
        noise = Sensor("6","ruido",getNoise(),True)
        air2 = Sensor("7","calidadAire2", getAirQ(),True)
        sensors = [presion,temp,air,humidity,metano,noise,air2]
        requestPost(getState(sensors))

def getState(sensors): 
    with open(dirJSON) as f:
            data = json.load(f)
            for item in data:
                for sensor in sensors:
                    if sensor.idSensor == item["_idSensor"]:
                        sensor.estado = item["_status"]
    return sensors

def requestPost(sensors):

    for sensor in sensors:
        
        now = datetime.datetime.now()

	""" Client RestFul """
	httplib2.debuglevel = 0
	http = httplib2.Http(timeout=4) 
	content_type_header = "application/json"

	url = URL_BASE + URL_API + URL_NAME_METHOD

	
	data = 	{
				"idSensor":sensor.idSensor,
                                "TipoSensor":sensor.tipo,
                                "Fecha": now.strftime("%Y-%m-%d"),
				"datoObtenido":sensor.valor,  
                                "Hora":now.strftime("%H:%M:%S")
			}

	headers = {'Content-Type': content_type_header}

	print ("Posting %s" % data)
        
        if sensor.valor != "-":
            if sensor.estado == True:
                try:
                    response, content = http.request(url, 'POST', json.dumps(data), headers=headers)
                    print(response)
                    print(content)
                except:
                    print("Error, no se pudo realizar la conexion con el servidor")
            else:
                print("estado del sensor false")
        else:
            print("valor del sensor no valido")



def main():

	getSensorData()
   


if __name__ == '__main__':

	main()


