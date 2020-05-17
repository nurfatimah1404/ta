import pandas as pd
#import influxdb
import time
from datetime import datetime
from datetime import datetime
from influxdb import InfluxDBClient
from influxdb import DataFrameClient
import requests
import json
    
client = InfluxDBClient('10.0.12.127', 8086, 'admin', '123456', 'NOAA_water_database')
q = "SELECT * from h2o_feet LIMIT 10"
df = pd.DataFrame(client.query(q, chunked=True, chunk_size=10000).get_points())
print (df)
#tes = df.to_json(orient='records')
#print (tes)
timeValues  = df[ ['col4'] ]
tags        = { 'col1': df[['col0']], 'col2': df[['col1']], 'col3':df[['col3']] }

dbConnDF = DataFrameClient('10.0.12.127', 8086, 'admin', '123456', 'mydb')
dbConnDF.write_points('mydb', 'olah', timeValues, tags = tags)
#timeValues.index  = df[ ['col0'] ]
#timeValues  = df[ ['mean'] ]
#timeValues.index  = df[ ['time'] ]
#dbConnDF = DataFrameClient('10.0.12.127', 8086, 'admin', '123456', 'NOAA_water_database')
#dbConnDF.write_points('NOAA_water_database', 'olahdat', timeValues)
#print("Finished writing to InfluxDB")
#client.write_points(tes, measurements='olah', protocol='line')