import sqlite3
from datetime import datetime
import os

def sqlDir():
    directory = 'db/'
    if not os.path.exists(directory):
        os.makedirs(directory)

def sqlWrite(topic, data, receivedTime):
    print(data)
    sensorTime, value, lat, lon, idSensor = data.split(',')
    now = datetime.now().strftime('%Y-%m-%d')
    conn = sqlite3.connect('db/{}.db'.format(now))
    
    c = conn.cursor()
    # Create table
    c.execute("CREATE TABLE IF NOT EXISTS data (sensorTime text NULL, receivedTime text NULL, topic TEXT, id TEXT, value TEXT, lat text NULL, long text NULL)")
    item = (sensorTime, receivedTime, topic, idSensor, value, lat, lon)
    c.execute("INSERT INTO data values ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(sensorTime, receivedTime, topic, idSensor, value, lat, lon))
    conn.commit()
    conn.close()