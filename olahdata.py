import pandas as pd
#import influxdb
from influxdb import InfluxDBClient
#client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
client = InfluxDBClient('10.0.12.127', 8086, 'admin', '123456', 'NOAA_water_database')
#client = InfluxDBClient(host='mydomain.com', port=8086, username='myuser', password='mypass' ssl=True, verify_ssl=True)
q = "SELECT MEAN(water_level) FROM h2o_feet GROUP BY time(1h) LIMIT 8"
#SELECT MEAN("water_level") FROM "h2o_feet" GROUP BY "location"
df = pd.DataFrame(client.query(q, chunked=True, chunk_size=10000).get_points())
print (df)
