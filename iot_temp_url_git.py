#!/usr/bin/env python

import urllib # for iot_temp_url
import RPi.GPIO as GPIO # for iot_temp_url, DHT11
import dht11  #for DHT11
from time import sleep #for DHT11 and iot_temp_url
import paho.mqtt.publish as publish #for DHT11
#Below is for DHT11
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

dht = dht11.DHT11(pin = 24)

mqttHost = "mqtt.thingspeak.com"
channelID = "Your_channel_ID"  #your thingspeak channelID
apiKey = "Your_apikey"   #your thinspeak apikey
tTransport = "websockets"
tPort = 80
tTLS = None
topic = "channels/" + channelID + "/publish/" + apiKey

def getSensorData():    
    r = dht.read()
    if r.is_valid():
        return(str(r.temperature), str(r.humidity))
    else:
        return(str(-1), str(-1))
#Above is for DHT11
#Below is for iot_temp
def fetch_thing(url, params, method):
    params = urllib.urlencode(params)
    if method=='POST':
        f = urllib.urlopen(url, params)
    else:
        f = urllib.urlopen(url+'?'+params)
    return (f.read(), f.code)
 #Above is for iot_temp  




#Below is for DHT11
while True:
    try:
        T, RH = getSensorData()
        print(T, RH)
        if T != '-1' and RH != '-1':
            tPayload = "field1=" + T + "&field2=" + RH            
            publish.single(topic, payload=tPayload, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
            #Below is for iot_temp
            temp= T
            print "[c=",temp,"]"
            content, response_code = fetch_thing(
                                     'http://x.x.x.x/settemp.php',#your IP and website
                                     {'id': 1, 'temp': temp},#collect data for your database(ex: mysql)
                                     'GET'
                                     ) 
            #Above is for iot_temp
            print "Sleeping for 3600 seconds."
            sleep(3600) #interval time of measuring temperature and humidity
        else:
            sleep(1)
    except:
        print('Error...')
        break       	  
#Above is for DHT11
