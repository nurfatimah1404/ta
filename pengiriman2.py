# Copyright (c) 2020 m4nzm333
# Source code for sending data log to server
# Source : https://github.com/m4nzm333/basestation-ta
# Ask a question, please contact:
# e-mail    : irman.mashuri@gmail.com
# hp/wa     : +6285396397688

import paho.mqtt.client as mqtt
import datetime as datetime
from time import sleep
# For testcase, delete later
from random import randint

# MQTT Setting
MQTT_Broker = "10.0.12.127"
MQTT_Port = 1883
mqtt_user = "admin"
mqtt_password = "123456"
Keep_Alive_Interval = 45

# Client object
mqttc = mqtt.Client("Basestation-0002")

# Publish Callback
def on_publish(client, userdata, result):
    print("Data published \n" + str(userdata))
    pass

# Try to connect callback
def on_connect(client, userdata, flag, rc):
    if rc==0:
        print("Connection successful\n")
    if rc==1:
        print("Connection refused - incorrect protocol version\n")
    if rc==2:
        print("Connection refused - invalid client identifier\n")
    if rc==3:
        print("Connection refused - server unavailable\n")
    if rc==4:
        print("Connection refused - not authorised\n")

# Assign Event Callbacks]
mqttc.on_publish = on_publish
mqttc.on_connect = on_connect

# Connect
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

# Publish (Topic, Data)
topicList = ["temperature", "pressure", "humidity", "PM_25","NH","NO2","CO2","CO","Asap","PM_10","SO2"]
idList = ["123abc","321abc","543xyz"]
latitudeList = ["-5.135399", "-4.123834"]
longitudeList = ["119.423790","231.912345"]

# Published data should be from data log
# data sample id=123456;temp=10;timestamp=2019-11-15-06:04:22.123123

# TODO : Data log reader algorithm

while 1:
    sleep(0.5)
    sampleTopic = topicList[randint(0, 10)]
    sampleid = idList[randint(0, 2)]
    sampleData = str(randint(30, 100))
    sampleLat = latitudeList[randint(0, 1)]
    sampleLong = longitudeList[randint(0, 1)]
    mqttc.publish(sampleTopic, sampleid+";"+ sampleData +";"+ sampleLat +";"+sampleLong)