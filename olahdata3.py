import pandas as pd
#import influxdb
import time
from datetime import datetime
from datetime import datetime
from influxdb import InfluxDBClient
from influxdb import DataFrameClient
import requests
import json
def read_db(NOAA_water_database,h2o_feet):
    # read  from database and fill data into pandas dataframe
    client = DataFrameClient(host = '10.0.12.127', port= 8086, user= 'admin', password = '123456', database= 'NOAA_water_database')
    result = client.query('SELECT MEAN(water_level) FROM + h2o_feet + GROUP BY time(1h) LIMIT 1', chunked=True)
    print (result)
    column = next(iter(result))
    data   = result[column]
    # convert utc time to local time
    #data.index = data.index.tz_convert('Europe/Berlin')
    # plotly tries to use utc time first, so remove timezone information:
    # https://github.com/plotly/plotly.py/blob/6f9621a611da36f10678c9d9c8c784f55e472429/plotly/utils.py#L263
    data.index = data.index.tz_localize(None)
    return data
    print ("finish")
    print (data)