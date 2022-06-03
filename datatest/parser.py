from datetime import datetime, timedelta
import random


def parseData():
    f = open('data.csv', 'r').read().splitlines()
    now = datetime.now()

    for row in f:
        co2, co, temp, hum, pm10, lat, lon, timeSensor, idSensor, end = row.split(
            ',')
        fNew = open('uji.csv', 'a')
        if temp == 'nan':
            continue
        if float(pm10) == 0:
            continue

        fNew.write('co2,{},{},{},{},{}\n'.format(timeSensor, co2, lat, lon, idSensor))
        fNew.write('co,{},{},{},{},{}\n'.format(timeSensor, co, lat, lon, idSensor))
        fNew.write('temperature,{},{},{},{},{}\n'.format(timeSensor, temp, lat, lon, idSensor))
        fNew.write('humidity,{},{},{},{},{}\n'.format(timeSensor, hum, lat, lon, idSensor))
        fNew.write('pm10,{},{},{},{},{}\n'.format(timeSensor, pm10, lat, lon, idSensor))
        fNew.close()

        now = now + timedelta(minutes=1, seconds=random.uniform(0, 59), milliseconds=random.uniform(0, 999))
        print(str(now))
        
parseData()
