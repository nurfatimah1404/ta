import datetime
import random
import time
import os
import csv
from csv import reader
from influxdb import client as influxdb
import argparse
import io
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



db = influxdb.InfluxDBClient("10.0.12.127", 8086, "admin", "123456", "coba")

#with open(filename) as f:
   # mylist = f.read().splitlines() 

#temp = open(filename,'r').read().split('\n')

def read_data(filename):
    print (filename)
    with open(filename) as f:
        lines = f.readlines()[1:]
        print(lines)
    return lines
    

if __name__ == '__main__':
    filename = r'/home/data/kualitas.txt'
    lines = read_data(filename)
    for rawline in lines:
        line = rawline.rstrip('\n').split(",")
        print (line)
        waktu = line[0]
        lat = line[6]
        longit = line[7]
        co = float(line[8])
        so = float(line[9])
        if(co<=0 or so<=0):
            print("Failed")
        else:
        #grades.append(lists[i].rstrip('\n').split(','))
        #EVERYTHING UP TO HERE WORKS. Not sure how to create the json below
        #====================================
            json_body = [
            {
                "measurement": "co",
                "time": waktu,
                "fields": {
                    "lat": lat,
                    "long": longit,
                    "value": co
                }
            },
            {
                "measurement": "so2",
                "time": waktu,
                "fields": {
                    "lat": lat,
                    "long": longit,
                    "value": so
                }
            }
            ]

            print (json_body)

            db.write_points(json_body)
            print("sukses")