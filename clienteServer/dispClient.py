#!/usr/bin/python3

import httplib2
import json
import time
import datetime


URL_BASE = "http://ec2-54-202-254-90.us-west-2.compute.amazonaws.com:8080/"
URL_API = "/backendAmbiente/webresources/generic/"
URL_NAME_METHOD = "saveMedicion"



def main():

	""" Client RestFul """
	httplib2.debuglevel = 0
	http = httplib2.Http() 
	content_type_header = "application/json"

	url = URL_BASE + URL_API + URL_NAME_METHOD

	data = 	{
				"idSensor":1,         
				"TipoSensor":"co2",   
				"Fecha":"2018-04-05",
				"datoObtenido":20.3,  
				"Hora":"11:00:00"
			}

	headers = {'Content-Type': content_type_header}
	print ("Posting %s" % data)

	response, content = http.request(url, 'POST', json.dumps(data), headers=headers)
	print(response)
	print(content)


if __name__ == '__main__':

	main()


