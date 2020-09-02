import pandas as pd
import time
from datetime import datetime
from datetime import datetime
from influxdb import InfluxDBClient
from influxdb import DataFrameClient
import requests   
client = InfluxDBClient('localhost', 8086, '', '', 'polusi2')
co = client.query("SELECT MEAN(value), STDDEV(value) FROM co GROUP BY time(1h)")
for data_point in co.get_points():
    if data_point['mean'] is not None :
        if data_point['mean'] <= 5:
            ia = float(50)
            ib = float(0)
            Xa = float(5)
            Xb = float(0)
        elif data_point['mean'] <= 10:
            ia = float(100)
            ib = float(50)
            Xa = float(10)
            Xb = float(5)
        elif data_point['mean'] <= 17:
            ia = float(200)
            ib = float(100)
            Xa = float(17)
            Xb = float(10)
        elif data_point['mean'] <= 34:
            ia = float(300)
            ib = float(200)
            Xa = float(34)
            Xb = float(17)
        elif data_point['mean'] <= 46:
            ia = float(400)
            ib = float(300)
            Xa = float(46)
            Xb = float(34)
        else:
            ia = float(500)
            ib = float(400)
            Xa = float(57.5)
            Xb = float(46)
        i = (float(ia) - float(ib)) / (float(Xa) - float(Xb)) * (float(data_point['mean']) - float(Xb)) + float(ib)
        print(i)
        data_to_write = [
                        {
                        "measurement" : "ho/co",
                        "time" : data_point['time'],
                        "tags" : {
                            "id" : "321abc"
                        },
                        "fields":  {
                            "rata_rata": data_point['mean'],
                            "std_deviasi" : data_point['stddev'],
                            "kategori": i_kat,
                            "longitude" : "231.912345",
                            "latitude" : "-4.123834"

                        }
                            }]
        client.write_points(data_to_write)
        print(data_to_write)
        print ("==================================")
        print("Finished writing to InfluxDB")
        print ("==================================")
    else:
        print("data none")
        
if i <= 50: 
    i_kat = "Baik"
elif i <= 100: 
    i_kat = "Sedang"
elif i <= 199: 
    i_kat = "Tidak Sehat"
elif i <= 299:
    i_kat = "Sangat Tidak Sehat"
else:
    i_kat = "Berbahaya"
print(i_kat)
