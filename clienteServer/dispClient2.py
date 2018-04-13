#!/usr/bin/python3

import httplib2
import json
import time
import datetime
from bmp085 import bmp085

URL_BASE = "http://ec2-54-202-254-90.us-west-2.compute.amazonaws.com:8080/"
URL_API = "/backendAmbiente/webresources/generic/"
URL_NAME_METHOD = "saveMedicion"


def getSensorData():

	pressure = bmp085.BMP085()

def requestPost():

	""" Client RestFul """
	httplib2.debuglevel = 0
	http = httplib2.Http() 
	content_type_header = "application/json"

	url = URL_BASE + URL_API + URL_NAME_METHOD

	
	data = 	{
				"idSensor":1,         
				"TipoSensor":"presionAtm",   
				"Fecha":"2018-04-05",
				"datoObtenido":2,  
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


