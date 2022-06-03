from datetime import datetime, timedelta
import random
import paho.mqtt.client as paho
import time

broker = "10.3.141.1"
port = 1883
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
id = "3F0D"
param = "temperature"
client1= paho.Client(id)                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker , port)
while True:
    now = str(datetime.now())
    lat = "-5.129954"
    lon = "119.481537"
    value = round(random.uniform(29.00, 35.00), 2)
    client1.publish(id+"/"+param, "{},{},{},{}".format(now, value, lat, lon))
    time.sleep(1)