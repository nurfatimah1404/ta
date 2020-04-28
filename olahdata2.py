import pandas as pd
import time
from datetime import datetime
from datetime import datetime
from influxdb import InfluxDBClient
from influxdb import DataFrameClient
import requests
import json
user = 'root'
password = 'root'
dbhost = "10.0.12.127"
dbport = 8086
dbuser = "admin"
dbpassword = "123456"
dbname = "mydb"
protocol = 'line'
measurement = "tes"
    
client = InfluxDBClient('10.0.12.127', 8086, 'admin', '123456', 'NOAA_water_database')
current_data = client.query("SELECT MEAN(water_level) FROM h2o_feet GROUP BY time(1h) LIMIT 1")
list_current_data = list(current_data.get_points())
for data_point in current_data.get_points():
    data_to_write = [{"measurement": "olah",
                    "fields": {"value1": data_point['time'],
                               "value2": data_point['mean']}
                    }]
    client.write_points(data_to_write)