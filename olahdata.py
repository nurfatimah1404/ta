import pandas as pd
from influxdb import InfluxDBClient   
dfclient = influxdb.DataFrameClient('10.0.12.127', 8086, 'admin', '123456', 'NOAA_water_dataabase')
q = "select * from h2o_feet"
df = pd.DataFrame(client.query('SELECT * FROM "h2o_feet" LIMIT 2'))
#client.query('SELECT "duration" FROM "pyexample"."autogen"."brushEvents" WHERE time > now() - 4d GROUP BY "user"')