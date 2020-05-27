import pandas as pd
#import influxdb
import time
from datetime import datetime
from datetime import datetime
from influxdb import InfluxDBClient
from influxdb import DataFrameClient
import requests
import json
    
clientx = InfluxDBClient('10.0.12.127', 8086, 'admin', '123456', 'mydb')
clienty = InfluxDBClient('10.0.12.127', 8086, 'admin', '123456', 'hasilolah')
#current_data = clientx.query("SELECT MEAN(value), stddev(value) FROM PM_10 GROUP BY time(1h)")
current_data = clientx.query("SELECT MEAN(value), stddev(value) FROM PM_10 where id='321abc' AND latitude='-4.123834' AND longitude='231.912345' AND time>='2020-05-09 00:59:14' group by time(1h)")
list_current_data = list(current_data.get_points())
print(list_current_data)
for data_point in current_data.get_points():
    if data_point['mean'] <=50 :
        x = "Baik"
    elif data_point['mean'] <=150 :
        x = "Sedang"
    elif data_point['mean'] <=350 :
        x = "Tidak Sehat"
    elif data_point['mean'] <=420 :
        x = "Sangat Tidak Sehat"
    elif data_point['mean'] >420  :
        x = "Berbahaya"
    data_to_write = [
                        {
                        "measurement" : "PM_10",
                        "time" : data_point['time'],
                        "tags" : {
                            "id" : "321abc"
                        },
                        "fields":  {
                            "rata_rata": data_point['mean'],
                            "std_deviasi" : data_point['stddev'],
                            "kategori": x,
                            "longitude" : "231.912345",
                            "latitude" : "-4.123834"

                        }
                    }]
    clienty.write_points(data_to_write)
    #print(data_to_write)
    print ("==================================")
    print("Finished writing to InfluxDB")
    print ("==================================")
#q = "SELECT * from h2o_feet LIMIT 10"
#df = pd.DataFrame(client.query(q, chunked=True, chunk_size=10000).get_points())
#print (df)
#tes = df.to_json(orient='records')
#print (tes)
#timeValues  = df[ ['time'] ]
#tags        = { 'col1': df[['level']], 'col2': df[['level description']], 'col3':df[['location']], 'col4':df[['water_level']] }

#dbConnDF = DataFrameClient('10.0.12.127', 8086, 'admin', '123456', 'mydb')
#dbConnDF.write_points('mydb', 'olah', timeValues, tags)
#timeValues.index  = df[ ['col0'] ]
#timeValues  = df[ ['mean'] ]
#timeValues.index  = df[ ['time'] ]
#dbConnDF = DataFrameClient('10.0.12.127', 8086, 'admin', '123456', 'NOAA_water_database')
#dbConnDF.write_points('NOAA_water_database', 'olahdat', timeValues)
#print("Finished writing to InfluxDB")
#client.write_points(df,'olah', protocol='line', time_precision="'s'")