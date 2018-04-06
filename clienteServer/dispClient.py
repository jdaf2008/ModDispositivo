#!/usr/bin/python3

import httplib2
import json
import time
import datetime
import MCP342X, wind_direction, HTU21D, bmp085, tgs2600, ds18b20_therm
import database

URL_BASE = "http://ec2-54-202-254-90.us-west-2.compute.amazonaws.com:8080/"
URL_API = "/backendAmbiente/webresources/generic/"
URL_NAME_METHOD = "saveMedicion"


def getSensorData():

	pressure = bmp085.BMP085()
	temp_probe = ds18b20_therm.DS18B20()
	air_qual = tgs2600.TGS2600(adc_channel = 0)
	humidity = HTU21D.HTU21D()
	wind_dir = wind_direction.wind_direction(adc_channel = 0, config_file="wind_direction.json")
	interrupts = interrupt_client.interrupt_client(port = 49501)

def requestPost():

	""" Client RestFul """
	httplib2.debuglevel = 0
	http = httplib2.Http() 
	content_type_header = "application/json"

	url = URL_BASE + URL_API + URL_NAME_METHOD

	
	data = 	{
				"idSensor":1,         
				"TipoSensor":,   
				"Fecha":"2018-04-05",
				"datoObtenido":20.3,  
				"Hora":"11:00:00"
			}

	headers = {'Content-Type': content_type_header}

	print ("Posting %s" % data)

	response, content = http.request(url, 'POST', json.dumps(data), headers=headers)
	print(response)
	print(content)



def main():

	getSensorData()
	requestPost()


if __name__ == '__main__':

	main()


