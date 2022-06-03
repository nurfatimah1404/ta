from datetime import datetime, timedelta
import random
import paho.mqtt.client as paho
import time

broker="192.168.1.240"
port=1883
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection

i = 0
delay = 1
f = open('uji.csv', 'r').read().splitlines()
for line in f:
    now = str(datetime.now())
    topic, timeSensor, value, lat, lon, idSensor = line.split(',')
    topic = idSensor+'/'+topic
    client1.publish(topic, '{},{},{},{}'.format(timeSensor,value, lat, lon))
    time.sleep(delay)
    i+= 1
    print(i)

   
    