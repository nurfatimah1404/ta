import os
from glob import glob
import datetime
import time
import argparse
from influxdb import client as influxdb
import shutil
import glob

db = influxdb.InfluxDBClient("182.23.82.22", 8086, "admin", "123456", "polusi")

# Baca Data
def read_data(filename):
    print(filename)
    with open(filename) as f:
        lines = f.readlines()[0:]
        #print(lines)
    return lines
# Split Data
def splitData(lineData):
    line2 = lineData.rstrip('\n').split(",")
    return line2

# Bikin Model Data
def dataDic(arrayData, tipeData):
    if tipeData == 'a':
        waktuA = arrayData[0]
        print(waktuA)
        co = float(arrayData[2])
        so2 = float(arrayData[3])
        pm10 = float(arrayData[4])
        lat = float(arrayData[5])
        longit = float(arrayData[6])
        idA = arrayData[7]
        if (co<=0 or so<=0 or pm10<=0 or lat==0 or longit==0):
            print("Failed")
        else:
            json_body = [
            {
                "measurement": "co",
                "time": waktuA,
                "tags": {
                    "id": idA
                },
                "fields": {
                    "latitude": lat,
                    "longitude": longit,
                    "value": co
                }
            },
            {
                "measurement": "so2",
                "time": waktuA,
                "tags": {
                    "id": idA
                },
                "fields": {
                    "latitude": lat,
                    "longitude": longit,
                    "value": so2
                }
            },
            {
                "measurement": "pm.10",
                "time": waktuA,
                "tags": {
                    "id": idA
                },
                "fields": {
                    "latitude": lat,
                    "longitude": longit,
                    "value": pm10
                }
            }
            ]

            print(json_body)
            db.write_points(json_body)
            print("Sukses fileA")
            print("=======================")
        #print('Bikin struktur A')
    if tipeData == 'b':
        waktuB = arrayData[0]
        temperature = float(arrayData[2])
        pressure = float(arrayData[3])
        height = float(arrayData[4])
        humidity = float(arrayData[5])
        idB = arrayData[6]
        if (temperature<=0 or so<=0 or pressure<=0 or height<=0 or humidity<=0):
            print("Failed")
        else:
            json_body = [
                {
                    "measurement": "temperature",
                    "time": waktuB,
                    "tags": {
                        "id": idB
                    },
                    "fields": {
                        "value": temperature
                    }
                },
                {
                    "measurement": "pressure",
                    "time": waktuB,
                    "tags": {
                        "id": idB
                    },
                    "fields": {
                        "value": pressure
                    }
                },
                {
                    "measurement": "height",
                    "time": waktuB,
                    "tags": {
                        "id": idB
                    },
                    "fields": {
                        "value": height
                    }
                },
                {
                    "measurement": "humidity",
                    "time": waktuB,
                    "tags": {
                        "id": idB
                    },
                    "fields": {
                        "value": humidity
                    }
                }

            ]
            print(json_body)
            db.write_points(json_body)
            print("Sukses fileB")
            print("=======================")

while True:
    folderDataku = os.listdir('/home/data/post2')
    for dataku in folderDataku:
        # folderFileku = os.listdir('/home/data/post/'+dataku)
        # for fileku in folderFileku:
        path = '/home/data/post2/'+dataku
        #print(path)
        tipe = path[-5:-4]
        print(tipe)
        lines = read_data(path)
        #print(lines)
        for line in lines:
            dataSplited = splitData(line)
            dataDic(dataSplited, tipe)

    source = '/home/data/post2/'
    dst = '/home/data/post/'
    files = glob.iglob(os.path.join(source, "*.txt"))
    #print(files)
    for file in files:
        shutil.move(file, dst)
        print("file berhasil dipindahkan")