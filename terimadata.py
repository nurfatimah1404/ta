#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import requests
import time
from datetime import datetime
from influxdb import InfluxDBClient
from SqlMonitor import sqlWrite
from config import influxServer, influxDBName
from CounterData import upBlocked, upReceived
from config import configTopic

# set influxDB configuration -----------------------------
dbhost = "182.23.82.22"
dbport = 8086
dbuser = "admin"
dbpassword = "123456"
dbname = influxDBName()
# ---------------------------------------------------
# set mqtt configuration ===========================
mqtt_server = "127.0.0.1"
mqtt_port = 1883
mqtt_user = "server-asd"
mqtt_password = ""
# =================================================


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # set client subscriber ----------------------
    client.subscribe(configTopic())
    # ----------------------------------------------


def on_message(client, userdata, msg):
    print("Received a message on topic: " + msg.topic)
    
    now = datetime.now()
    receiveTime = str(now)

    message = msg.payload.decode("utf-8")

    idSensor, topic = msg.topic.split('/')
    sensorTime, value, lat, longit = message.split(',')

    value = float(value)
    print("------------------")
    print("Receive Time : "+receiveTime)
    print("Sensor Time : "+sensorTime)
    print(idSensor)
    print(value)
    print(lat)
    print(longit)
    print("------------------")

    # Tambahkan data pada SQLite
    sqlWrite(msg.topic, message, receiveTime)

    if idSensor == '025f' and sensorTime is not None and (value > 0 or value is not None):
        json_body = [
            {
                "measurement": topic,
                "time": sensorTime,
                "tags": {
                    "id": idSensor
                },
                "fields": {
                    "value": float(value)
                }
            }
        ]
        upReceived()
        if influxServer():
            dbclient.write_points(json_body)
            print("Finished writing to InfluxDB")
            print("==================================") 
    elif sensorTime is not None and (value > 0 or value is not None) and (lat != '' and longit != ''):
        json_body = [
            {
                "measurement": topic,
                "time": sensorTime,
                "tags": {
                    "id": idSensor
                },
                "fields": {
                    "latitude": float(lat),
                    "longitude": float(longit),
                    "value": float(value)
                }
            }
        ]
        upReceived()
        print("Tipe 2")
        if influxServer():
            dbclient.write_points(json_body)
            print("Finished writing to InfluxDB")
            print("==================================")
    else:
        upBlocked()
        print("Failed Writing to InfluxDB")


        # client.publish("demo")
# ====================================================
# Set up a client for InfluxDB
dbclient = InfluxDBClient(dbhost, dbport, dbuser, dbpassword, dbname)

# ====================================================
# Initialize the MQTT client that should connect to the Mosquitto broker
client = mqtt.Client('server-ima')
client.on_connect = on_connect
client.on_message = on_message
client.connect('127.0.0.1', 1883, 30)
client.loop_forever()
