#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import requests
import time
from datetime import datetime
from influxdb import InfluxDBClient
# set influxDB configuration -----------------------------
dbhost = "10.0.12.127"
dbport = 8086
dbuser = "admin"
dbpassword = "123456"
dbname = "mydb"
#---------------------------------------------------
# set mqtt configuration ===========================
mqtt_server = "10.0.12.127"
mqtt_port = 1883
mqtt_user = "admin"
mqtt_password = "123456"
# =================================================
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
# set client subscriber ----------------------
    client.subscribe("temperature")
    client.subscribe("pressure")
    client.subscribe("humidity")
    client.subscribe("PM_2.5")
    client.subscribe("NH")  
    client.subscribe("NO2")  
    client.subscribe("CO2")
    client.subscribe("CO")
    client.subscribe("Asap")
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
def on_message(client, userdata, msg):
    print("Received a message on topic: " + msg.topic)
# Use utc as timestamp
    now = datetime.now()
    receiveTime = now.strftime("%Y-%m-%d %H:%M:%S")
#receiveTime=datetime.datetime.utcnow()
    message=msg.payload.decode("utf-8")
    id, sample, time = message.split(";")
    print("------------------")
    print("Receive Time : "+receiveTime)
    print(id)
    print(sample)
    print(time)
    print("------------------")

    if(id is None or sample is None or time is None):
        print("Failed writing to InfluxDB")
    else:
        json_body = [
            {
                "measurement": msg.topic,
                "time": str(time),
                "fields": {
                    "id": id,
                    "value" : float(sample)
                } 
            }
        ]
        dbclient.write_points(json_body)
        print("Finished writing to InfluxDB")
        print ("==================================")
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