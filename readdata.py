import os
from glob import glob
import datetime
import time
import argparse
from influxdb import client as influxdb
import shutil
import glob

db = influxdb.InfluxDBClient("10.0.12.127", 8086, "admin", "123456", "polusi")

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
        temperature = float(arrayData[1])
        tek = float(arrayData[2])
        kel = float(arrayData[3])
        pm = float(arrayData[4])
        idA = arrayData[5]
        if (suhu<=0 or kel<=0 or tek<=0 or pm<=0):
            print("Failed")
        else:
            json_body = [
            {
                "measurement": "temperature",
                "time": waktuA,
                "tags": {
                    "id": idA
                },
                "fields": {
                    "value": temperature,
                }
            },
            {
                "measurement": "pressure",
                "time": waktuA,
                "tags": {
                    "id": idA
                },
                "fields": {
                    "value": tek,
                }
            },
            {
                "measurement": "humidity",
                "time": waktuA,
                "tags": {
                    "id": idA
                },
                "fields": {
                    "value": kel,
                }
            },
            {
                "measurement": "pm25",
                "time": waktuA,
                "tags": {
                    "id": idA
                },
                "fields": {
                    "value": pm,
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
        lat = float(arrayData[2])
        long = float(arrayData[3])
        co = float(arrayData[4])
        so = float(arrayData[5])
        idB = arrayData[6]
        if (co<=0 or so<=0):
            print("Failed")
        else:
            json_body = [
                {
                    "measurement": "co",
                    "time": waktuB,
                    "tags": {
                        "id": idB
                    },
                    "fields": {
                        "latitude": lat,
                        "longitude": long,
                        "value": co
                    }
                },
                {
                    "measurement": "so2",
                    "time": waktuB,
                    "tags": {
                        "id": idB
                    },
                    "fields": {
                        "latitude": lat,
                        "longitude": long,
                        "value": so
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