import pandas as pd
#import influxdb
import time
from datetime import datetime
from datetime import datetime
from influxdb import InfluxDBClient
from influxdb import DataFrameClient
import requests
import json
    
#client = InfluxDBClient('10.0.12.127', 8086, 'admin', '123456', 'NOAA_water_database')
#q = "SELECT MEAN(water_level) FROM h2o_feet GROUP BY time(1h) LIMIT 1"
#df = pd.DataFrame(client.query(q, chunked=True, chunk_size=10000).get_points())
#print (df)
#tes = df.to_json(orient='records')
#print (tes)
#timeValues  = df[ ['mean'] ]
#timeValues.index  = df[ ['time'] ]
#dbConnDF = DataFrameClient('10.0.12.127', 8086, 'admin', '123456', 'NOAA_water_database')
#dbConnDF.write_points('NOAA_water_database', 'olahdat', timeValues)
#print("Finished writing to InfluxDB")
client = DataFrameClient(
    '10.0.12.127', # DB server hostname
    8086, # DB server port
    'admin', # DB user
    '123456', # Password
    'mydb' # DB name
)
# Here we fetch the execution timings for a hypothetical JSON RPC method
# providing registration to the service. This uses InfluxQL.
# NOTE: This function returns a Pandas dataframe!
res = client.query(f'select * from temperature')
res = res['rpc_api.register']