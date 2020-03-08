#!/usr/bin/env python3
#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import requests
from io import StringIO
import time
import os
import json
from datetime import datetime
from influxdb import InfluxDBClient
#====================================================
# set influxdb configuration -------------------------
dbhost = "10.0.12.127"
dbport = 8086
dbuser = "admin"
dbpassword = "123456"
dbname = "mydb"

#====================================================
# set mqtt configuration ===========================
mqtt_server = "10.0.12.127"
mqtt_port = 1883
mqtt_user = "admin"
mqtt_password = "123456"
# =================================================    
#====================================================

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
# set client subscriber ----------------------
    client.subscribe("temperature")
    client.subscribe("humidity")
    client.subscribe("PM_2.5")
    client.subscribe("NH")  
    client.subscribe("NO2")  
    client.subscribe("CO2")
    client.subscribe("CO")
    client.subscribe("Asap")
        
#    client.subscribe("demo")
#====================================================
def on_message(client, userdata, msg):
    print("Received a message on topic: " + msg.topic)
    # Use utc as timestamp
    now = datetime.now()
    receiveTime = now.strftime("%Y-%m-%d %H:%M:%S")
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    print("data Received type",type(m_decode))
    print("data Received",m_decode)
    print("Converting from Json to Object")
    m_in=json.loads(m_decode) #decode json data
    print(type(m_in))
    print("id = ",m_in["id"])
    print(m_decode["id"])
    print(m_decode['id'])
    #print("broker 2 address = ",m_in["broker2"])
    #receiveTime=datetime.datetime.utcnow()
    #message=msg.payload.decode("utf-8")
    
    #data = json.loads(msg.payload.decode("utf-8"))
    #print (data)
    #x = data['id']
    #y = data['sampleTopic'] 
    #z = data['sampleData']
    #a = data['timestamp'] 
    #isfloatValue=False   
    #print (x)
    #print (y)

    try:
        # Convert the string to a float so that it is stored as a number and not a string in the database
        val = float(data)
        isfloatValue=True
    except:
        print("Could not convert " + data + " to a float value")
        isfloatValue=False

    if isfloatValue:
        print(str(receiveTime) + ": " + msg.topic + " " + str(val))
            
        if (msg.topic == "temperature"):            
            json_data = [
                {
                    "measurement": msg.topic,
                    "time": str(receiveTime),
                    "tags": {
                        "id": "abc123"
                    },
                    "fields": {
                        "temperature": val
                    }
                }
            ]
            
        if (msg.topic == "humidity"):              
            json_data = [
                {
                    "measurement": msg.topic,
                    "time": str(receiveTime),
                    "tags": {
                        "id": "abc13456"
                    },
                    "fields": {
                        "humidity": val
                    }
                }
            ]

        if (msg.topic == "PM_2.5"):                   
            json_data = [
                {
                    "measurement": msg.topic,
                    "time": str(receiveTime),
                    "tags": {
                        "id": "123456"
                    },
                    "fields": {
                        "PM_2.5": val
                    }
                }
            ]

        if (msg.topic == "NH"):                   
            json_data = [
                {
                    "measurement": msg.topic,
                    "time": str(receiveTime),
                    "tags": {
                        "id": "123456"
                    },
                    "fields": {
                        "NH": val
                    }
                }
            ]

        if (msg.topic == "N02"):                   
            json_data = [
                {
                    "measurement": msg.topic,
                    "time": str(receiveTime),
                    "tags": {
                        "id": "123456"
                    },
                    "fields": {
                        "NO2": val
                    }
                }
            ]

        if (msg.topic == "CO2"):                   
            json_data = [
                {
                    "measurement": msg.topic,
                    "time": str(receiveTime),
                    "tags": {
                        "id": "123456"
                    },
                    "fields": {
                        "CO2": val
                    }
                }
            ]

        if (msg.topic == "CO"):                   
            json_data = [
                {
                    "measurement": msg.topic,
                    "time": str(receiveTime),
                    "tags": {
                        "id": "123456"
                    },
                    "fields": {
                        "CO": val
                    }                   
                }
            ]
            
        if (msg.topic == "Asap"):                   
            json_data = [
                {
                    "measurement": msg.topic,
                    "time": str(receiveTime),
                    "tags": {
                        "id": "123456"
                    },
                    "fields": {
                        "Asap": val
                    }
                }
            ]
       # saveData(msg.topic, message)
        #print("Finished writing to File !!!") 
        #dbClient.create_database(dbname)
        dbclient.write_points(json_data)
        print("Finished writing to InfluxDB")
        print("Waiting data from client...")
#   client.publish("demo")
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
    time.sleep(10)
#====================================================
# Blocking loop to the Mosquitto broker
client.loop_forever()