import sqlite3
from datetime import datetime
import os

def sqlDir():
    directory = 'db/'
    if not os.path.exists(directory):
        os.makedirs(directory)

def sqlWrite(topic, data, receivedTime):
    sqlDir()
    sensorTime, receivedTime, value, lat, lon, idSensor = data.split(',')
    recTime = datetime.strptime(
    receivedTime, "%Y-%m-%d %H:%M:%S.%f")

    conn = sqlite3.connect(
        './db/{}-{}-{}.db'.format(recTime.year, recTime.month, recTime.day))
    c = conn.cursor()
    # Create table
    c.execute("CREATE TABLE IF NOT EXISTS '%s' (sensorTime text NULL, receivedTime text NULL, id, value, lat NULL, long NULL)" % topic)
    item = (sensorTime, receivedTime, idSensor, value, lat, lon)
    c.execute("INSERT INTO '%s' values (?, ?, ?, ?, ?, ?)" %
            topic, item)
    conn.commit()
    conn.close()