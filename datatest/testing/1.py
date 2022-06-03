from datetime import datetime, timedelta
import random
import paho.mqtt.client as paho
import time

broker = "192.168.1.240"
port = 1883
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
id = "015e"
param = "pm10"
client1= paho.Client(id)                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker , port)
blocked = 0
while True:
    now = str(datetime.now())
    lat = "-5.129954"
    lon = "119.481537"
    value = round(random.uniform(600, 1000), 2)
    client1.publish(id+"/"+param, "{},{},{},{}".format(now, value, lat, lon))
    blocked += 1
    if blocked == 17:
        client1.publish(id+"/"+param, "{},{},{},{}".format(now, 'nan', lat, lon))
    time.sleep(1)