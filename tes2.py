#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import requests
import time
import json
from datetime import datetime
from influxdb import InfluxDBClient
# set influxDB configuration -----------------------------
dbhost = "10.0.12.127"
dbport = 8086
dbuser = ""
dbpassword = ""
dbname = "mydb"
#---------------------------------------------------
# set mqtt configuration ===========================
mqtt_server = "10.0.12.127"
mqtt_port = 1883
mqtt_user = ""
mqtt_password = ""
# =================================================
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
# set client subscriber ----------------------
    client.subscribe("bme/humidity")
    client.subscribe("bme/temperature_F")
    client.subscribe("bme/temperature_C")
    client.subscribe("bme/pressure")
    client.subscribe("rainsensor/rainfall")
    client.subscribe("Wind/wind_direction")
    client.subscribe("Wind/wind_speed")
# panel surya---------------------------------
    client.subscribe("Cap/Bateray")
    client.subscribe("RELAY/Relay")
    client.subscribe("BH1750/Light")
    client.subscribe("TEMPERATUR/celcius")
    client.subscribe("INA219/busvoltage_C")
    client.subscribe("INA219/shuntvoltage_C")
    client.subscribe("INA219/current_mA_C")
    client.subscribe("INA219/power_mW_C")
    client.subscribe("INA219/loadvoltage_C")
    client.subscribe("INA219/busvoltage_B")
    client.subscribe("INA219/shuntvoltage_B")
    client.subscribe("INA219/current_mA_B")
    client.subscribe("INA219/power_mW_B")
    client.subscribe("INA219/loadvoltage_B")
#----------------------------------------------
#def on_message(client, userdata, msg):
    #message = str(msg.payload)
    #if is_json(message): 
        #jsonResponse=json.loads(message)
        #print (jsonResponse)
def on_message(client, userdata, message):
    print("MESSAGE")
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    received=message.payload.decode("utf-8","ignore")
    received=json.loads(received) #JSON data to python object
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
connOK=False

while(connOK == False):
    try:
        client.username_pw_set(mqtt_user, mqtt_password)
        client.connect(mqtt_server, mqtt_port, 60)
        connOK = True

    except:
        connOK = False
    time.sleep(2)
# Blocking loop to the Mosquitto broker
client.loop_forever()