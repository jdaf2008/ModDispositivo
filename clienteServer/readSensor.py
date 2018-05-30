#!/usr/bin/python3

import serial

def getMetano():
	lecture = main()
	return lecture[0];

def getNoise():
	lecture = main()
	return lecture[1];

def getAirQ():
	lecture = main()
	return lecture[2]

def main():

	ser = serial.Serial("/dev/ttyACM0",9600)
	try:
		data = ser.readline()
		data1 = data.splitlines() 
		data2 = data1[0].split(',')
		return data2
	except ValueError:    		
		print('error')
 



