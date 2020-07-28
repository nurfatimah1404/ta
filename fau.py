import datetime
import random
import time
import os
import csv
from csv import reader
import argparse
from influxdb import client as influxdb
from glob import glob
#print(glob.glob("C:\Users\acer\txt\*.txt"))


db = influxdb.InfluxDBClient("10.0.12.127", 8086, "admin", "123456", "polusi2")

def read_data(filename):
    print (filename)
    with open(filename) as f:
        lines = f.readlines()[1:]
        print(lines)
    return lines
    

if __name__ == '__main__':
    filename = glob(r"/home/data/post/tes/*.csv")[0]
    #filename = glob("MAIN/DATA/*.csv")[0]
    lines = read_data(filename)
    for rawline in lines:
        line = rawline.rstrip('\n').split(",")
        print (line)
        #grades.append(lists[i].rstrip('\n').split(','))
        co2 = float(line[0])
        co = float(line[1])
        tem = float(line[2])
        hum = float(line[3])
        pm = float(line[4])
        lat = float(line[5])
        longit = float(line[6])
        waktu = line[7]
        idx = line[8]
        
        #EVERYTHING UP TO HERE WORKS. Not sure how to create the json below
            #====================================
        json_body = [
        {
            "measurement": "co",
            "time": waktu,
            "tags": {
                "id": idx
            },
            "fields": {
                "long": longit,
                "lang": lat,
                "value": co
            }
        },
            {
            "measurement": "co2",
            "time": waktu,
            "tags": {
                "id": idx
            },
            "fields": {
                "long": longit,
                "lang": lat,
                "value": co2
            }
        },
            {
            "measurement": "temperature",
            "time": waktu,
            "tags": {
                "id": idx
            },
            "fields": {
                "long": longit,
                "lang": lat,
                "value": tem
            }
        },
            {
            "measurement": "humidity",
            "time": waktu,
            "tags": {
                "id": idx
            },
            "fields": {
                "long": longit,
                "lang": lat,
                "value": hum
            }
        },
            {
            "measurement": "pm25",
            "time": waktu,
            "tags": {
                "id": idx
            },
            "fields": {
                "long": longit,
                "lang": lat,
                "value": pm
            }
        }
        ]

        print(json_body)
        db.write_points(json_body)
        print("sukses")