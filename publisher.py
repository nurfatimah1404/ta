#!/usr/bin/env python

import paho.mqtt.client as mqtt
import time

# This is the Publisher
mqtt_server = "10.0.12.127"
mqtt_port = 1883
mqtt_user = "admin"
mqtt_password = "123456"
#================================
connOK = True

temperature = 25
humidity = 75
pressure= 250
PM_25= 55
NH = 35
NO2 = 40
CO2 = 35
CO = 50
Asap = 30
PM_10 = 40
SO2 = 45

time_sleep = 5

# create client object
client = mqtt.Client()

while(connOK == True):
    try:
        client.username_pw_set(mqtt_user, mqtt_password)
        client.connect(mqtt_server, mqtt_port, 60)
#        connOK = False
        if temperature >= 40:
            connOK = False
	    temperature = 0	

        client.publish("temperature", temperature)
        client.publish("humidity", humidity)
        client.publish("pressure", pressure)
        client.publish("PM_25", PM_25)
        client.publish("NH", NH)
        client.publish("NO2", NO2)
        client.publish("CO2", CO2)
        client.publish("CO", CO)
        client.publish("Asap", Asap)
        client.publish("PM_10", PM_10)
        client.publish("SO2", SO2)


        print "Sending temperature : ",temperature
        print "Sending humidity : ",humidity
        print "Sending moisture : ",pressure
        print "Sending moisture : ",PM_25
        print "Sending moisture : ",NH
        print "Sending moisture : ",NO2
        print "Sending moisture : ",CO2
        print "Sending moisture : ",CO
        print "Sending moisture : ",Asap
        print "Sending moisture : ",PM_10
        print "Sending moisture : ",SO2
        print "-------------------------------------"

#       client.subscribe("demo")

    except:
        connOK = True
    time.sleep(time_sleep)
    temperature += 1
    humidity += 1
    pressure += 5
    #moisture += 5

# Blocking loop
if connOK == False:
   client.disconnect()
else:
   client.loop_forever()

