import datetime
import random
import time
import os
import csv
from csv import reader
from influxdb import client as influxdb
import argparse
import io
#from importlib import reload
import sys
from glob import glob

db = influxdb.InfluxDBClient("10.0.12.127", 8086, "admin", "123456", "file")

def read_data(filename):
    print (filename)
    with open(filename) as f:
        lines = f.readlines()[1:]
        print(lines)
    return lines
    
if __name__ == '__main__':
    filename = glob(r'/home/data/*.txt')[0]
    lines = read_data(filename)
    for rawline in lines:
        line = rawline.rstrip('\n').split(",")
        print (line)
       
        
       # if(co<=0 or so<=0):
        #    print("Failed")
        
        #grades.append(lists[i].rstrip('\n').split(','))
        #EVERYTHING UP TO HERE WORKS. Not sure how to create the json below
        #====================================
            