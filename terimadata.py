#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import requests
import time
from datetime import datetime
from influxdb import InfluxDBClient
from SqlMonitor import SqlMonitor
# set influxDB configuration -----------------------------
dbhost = "182.23.82.22"
dbport = 8086
dbuser = "admin"
dbpassword = "123456"
dbname = "tes"
#---------------------------------------------------
# set mqtt configuration ===========================
mqtt_server = "127.0.0.1"
mqtt_port = 1883
mqtt_user = "server-asd"
mqtt_password = ""
# =================================================

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
# set client subscriber ----------------------
    client.subscribe("temperature")
    client.subscribe("pressure")
    client.subscribe("humidity")
    client.subscribe("pm25")
    client.subscribe("co2")
    client.subscribe("co")
    client.subscribe("pm10")
    client.subscribe("so")

#----------------------------------------------
def on_message(client, userdata, msg):
    print("Received a message on topic: " + msg.topic)
# Use utc as timestamp
    now = datetime.now()
    receiveTime = str(now)
#receiveTime=datetime.datetime.utcnow()
    message=msg.payload.decode("utf-8")
    # Debug
    # id, myTopic, value, lat, longit, sensorTime, sendTime = message.split(",")
    # Data asli
    # sensorTime, value, lat, longit, id = message.split(',')
    sensorTime, value, lat, longit, id = message.split(',')
    value = float(value)
    print("------------------")
    print("Receive Time : "+receiveTime)
    print("Sensor Time : "+sensorTime)
    print(id)
    print(value)
    print(lat)
    print(longit)
    print("------------------")

    SqlMonitor.sqlWrite(msg.topic, message, receiveTime)

    
    if id == '025f' and value >0 or value is not None or sensorTime is not None or sensorTime >0:
        json_body = [
            {
                "measurement": msg.topic,
                "time": sensorTime,
                "tags": {
                    "id" : id
                },
                "fields": {                   
                    "value" : float(value)
                } 
            }
        ]
        dbclient.write_points(json_body)
        print("Finished writing to InfluxDB")
        print ("==================================")
    elif value >0 or value is not None or sensorTime is not None or sensorTime >0:
        json_body = [
            {
                "measurement": msg.topic,
                "time": sensorTime,
                "tags": {
                    "id" : id
                },
                "fields": {
                    "latitude" : float(lat),
                    "longitude" : float(longit),                    
                    "value" : float(value)
                } 
            }
        ]
        dbclient.write_points(json_body)
        print("Finished writing to InfluxDB")
        print ("==================================")
    else:
        print ("Failed Writing to InfluxDB")
        #client.publish("demo")
#====================================================        
# Set up a client for InfluxDB
dbclient = InfluxDBClient(dbhost, dbport, dbuser, dbpassword, dbname)

#====================================================
# Initialize the MQTT client that should connect to the Mosquitto broker
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
#====================================================
# Blocking loop to the Mosquitto broker
client.loop_forever()
