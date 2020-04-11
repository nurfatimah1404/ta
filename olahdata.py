import pandas as pd
#import influxdb
import time
from datetime import datetime
from influxdb import InfluxDBClient
#client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
dbhost = "10.0.12.127"
dbport = 8086
dbuser = "admin"
dbpassword = "123456"
dbname = "mydb"
dbclient = InfluxDBClient(dbhost, dbport, dbuser, dbpassword, dbname)
client = InfluxDBClient('10.0.12.127', 8086, 'admin', '123456', 'NOAA_water_database')
#client = InfluxDBClient(host='mydomain.com', port=8086, username='myuser', password='mypass' ssl=True, verify_ssl=True)
q = "SELECT MEAN(water_level) FROM h2o_feet GROUP BY time(1h) LIMIT 8"
#SELECT MEAN("water_level") FROM "h2o_feet" GROUP BY "location"
df = pd.DataFrame(client.query(q, chunked=True, chunk_size=10000).get_points())
print (df)
time = df.iloc[:,1]
mean = df.iloc[:,0]
client.write_points(result, tags={'mean': pd[['mean']]}, database='NOAA_water_database', measurement='olahh2o')
#print(df.loc[[159220]])
