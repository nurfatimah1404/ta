#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import requests
import time
from datetime import datetime
from SqlMonitor import sqlWrite
from config import influxServer, influxDBName, configTopic
from CounterData import upBlocked, upReceived
from includes.Datalog import logWrite

# ---------------------------------------------------
# set mqtt configuration ===========================
mqtt_server = "127.0.0.1"
mqtt_port = 1883
mqtt_user = "server-asd"
mqtt_password = ""
# =================================================


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    print(configTopic())
    client.subscribe(configTopic())

def on_message(client, userdata, msg):
    print("Received a message on topic: " + msg.topic)
    now = datetime.now()
    receiveTime = str(now)
    message = msg.payload.decode("utf-8")
    
    idSensor, param = msg.topic.split('/')
    sensorTime, value, lat, longit = message.split(',')
    
    value = float(value)
    logWrite(param, receiveTime+','+message+','+idSensor)
    print("------------------")
    print("Receive Time : "+receiveTime)
    print("Sensor Time : "+sensorTime)
    print(idSensor)
    print(value)
    print(lat)
    print(longit)
    print("------------------")

# ====================================================
# Initialize the MQTT client that should connect to the Mosquitto broker
client = mqtt.Client('server-ima')
client.on_connect = on_connect
client.on_message = on_message
client.connect('127.0.0.1', 1883, 30)
client.loop_forever()