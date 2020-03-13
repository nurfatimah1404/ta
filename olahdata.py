import pandas as pd
import influxdb
client = influxdb.InfluxDBClient('10.0.12.127', 8086, 'admin', '123456', 'NOAA_water_dataabase')
q = "select * from h2o_feet LIMIT 2"
print (q)
df = pd.DataFrame(client.query(q, chunked=True, chunk_size=10000).get_points())