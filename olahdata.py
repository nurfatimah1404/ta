import pandas as pd
#import influxdb
import time
from datetime import datetime
from datetime import datetime
from influxdb import InfluxDBClient
from influxdb import DataFrameClient
import requests
import json
#def main(host='localhost', port=8086):
#"""Instantiate the connection to the InfluxDB client."""
user = 'root'
password = 'root'
dbhost = "10.0.12.127"
dbport = 8086
dbuser = "admin"
dbpassword = "123456"
dbname = "mydb"
protocol = 'line'
measurement = "tes"
    
clienta = DataFrameClient('10.0.12.127', 8086, 'admin', '123456', 'NOAA_water_database')
clientb = InfluxDBClient('10.0.12.127', 8086, 'admin', '123456', 'mydb')
#client = InfluxDBClient(host='mydomain.com', port=8086, username='myuser', password='mypass' ssl=True, verify_ssl=True)
q = "SELECT MEAN(water_level) FROM h2o_feet GROUP BY time(1h) LIMIT 1"
#SELECT MEAN("water_level") FROM "h2o_feet" GROUP BY "location"
result = clienta.query(q)
for point in result.get_points():
    print (point)
#client.write_points(point,'tes')

df = pd.DataFrame(clienta.query(q, chunked=True, chunk_size=10000).get_points())
df["time"] = pd.to_datetime(df["time"], format="%Y-%m-%dT%H:%M:%SZ")
#df["time"].replace("T", " ").replace("Z", "")
#result = pd.DataFrame(client.query(q, chunked=False).raw)
#print (result)
print (df)
#tes = df['time'].dt.tz_localize(None)
#has = df['time'].str.strip(' T Z')
#print (tes)
