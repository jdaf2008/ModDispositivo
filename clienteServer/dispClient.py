#!/usr/bin/python3

import httplib2
import json
import time
import datetime
from Sensor import Sensor
from readSensor import getNoise, getAirQ, getMetano
import interrupt_client, MCP342X, wind_direction, HTU21D, bmp085, tgs2600, ds18b20_therm

URL_BASE = "http://ec2-54-202-254-90.us-west-2.compute.amazonaws.com:8080/"
URL_API = "/backendAmbiente/webresources/generic/"
URL_NAME_METHOD = "saveMedicion"


def getSensorData():

        presion = Sensor("1","presion",bmp085.BMP085().get_pressure())
        requestPost(presion);
        temp = Sensor("2","temperatura", ds18b20_therm.DS18B20().read_temp())
        requestPost(temp)
        air = Sensor("3","calidadAire",tgs2600.TGS2600(adc_channel = 0).get_value())
        requestPost(air)
        humidity = Sensor("4","humedad",HTU21D.HTU21D().read_temperature())
	requestPost(humidity)
        metano = Sensor("5", "metano",getMetano())
        requestPost(metano)
        noise = Sensor("6","ruido",getNoise())
        requestPost(noise)
        air2 = Sensor("7","calidadAire2", getAirQ())
        requestPost(air2)

def requestPost(sensor):

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


