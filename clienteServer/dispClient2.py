#!/usr/bin/python3

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


def getSensorData():

        presion = Sensor("1","presion",bmp085.BMP085().get_pressure(),"null")
        temp = Sensor("2","temperatura", ds18b20_therm.DS18B20().read_temp(),"null")
        air = Sensor("3","calidadAire",tgs2600.TGS2600(adc_channel = 0).get_value(),"null")
        humidity = Sensor("4","humedad",HTU21D.HTU21D().read_temperature(),"null")
        metano = Sensor("5", "metano",getMetano(),"null")
        noise = Sensor("6","ruido",getNoise(),"null")
        air2 = Sensor("7","calidadAire2", getAirQ(),"null")
        sensors = [presion,temp,air,humidity,metano,noise,air2]
        requestPost(sensors)

def getState(sensors):

    with open('testSensores.JSON') as f:
            data = json.load(f)
            for item in data:
                for sensor in sensors:
                    if sensor.idSensor == item["_idSensor"]:
                        sensor.estado = item["_status"]
                        print(item["_status"])
    return sensors

def requestPost(sensors):

    for sensor in sensors:

        now = datetime.datetime.now()

	""" Client RestFul """
	httplib2.debuglevel = 0
	http = httplib2.Http() 
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

	response, content = http.request(url, 'POST', json.dumps(data), headers=headers)
	print(response)
	print(content)



def main():

	getSensorData()
   


if __name__ == '__main__':

	main()


