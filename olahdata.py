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
#client = InfluxDBClient(host='mydomain.com', port=8086, username='myuser', password='mypass' ssl=True, verify_ssl=True)
q = "SELECT MEAN(water_level) FROM h2o_feet GROUP BY time(1h) LIMIT 1"

df = pd.DataFrame(client.query(q, chunked=True, chunk_size=10000).get_points())
#df["time"] = pd.to_datetime(df["time"], format="%Y-%m-%dT%H:%M:%SZ")
print (df)
#tes = df['time'].dt.tz_localize(None)
#tes = df.to_json(orient='records')
#print (tes)
#time = df.iloc[:,1]
#mean = df.iloc[:,0]
#timeValues = df[ ['time'] ]
#timeValues.index = df[ ['mean'] ]
#print (timeValues)
#tags = { 'mean': df[['mean']] }
data_to_write = [
                        {
                        "measurement" : "olahdat",
                        "time" : df.iloc[:,1],
                        "fields":  {
                            "value": df['mean']
                        }
                    }]
client.write_points(data_to_write)
print("Finished writing to InfluxDB")
