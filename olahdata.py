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
def main(host='10.0.12.127', port=8086):
    """Instantiate the connection to the InfluxDB client."""
    user = 'admin'
    password = '123456'
    dbname = 'mydb'
    protocol = 'line'

    client = DataFrameClient(host, port, user, password, dbname)

    print("Create pandas DataFrame")
    df = pd.DataFrame(data=list(range(30)),
                      index=pd.date_range(start='2020-05-09',
                                          periods=30, freq='H'), columns=['0'])

    print(df)
    print("Write DataFrame")
    client.write_points(df, 'demo', protocol=protocol)
    

    #print("Write DataFrame with Tags")
    #client.write_points(df, 'demo',
     #                   {'k1': 'v1', 'k2': 'v2'}, protocol=protocol)

    #print("Read DataFrame")
    #client.query("select * from demo")

    #print("Delete database: " + dbname)
    #client.drop_database(dbname)