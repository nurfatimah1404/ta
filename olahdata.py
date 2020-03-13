import pandas as pd
#import influxdb
from influxdb import InfluxDBClient
# set influxDB configuration -----------------------------
dbhost = "10.0.12.127"
dbport = 8086
dbuser = "admin"
dbpassword = "123456"
dbname = "NOAA_water_database"
#client = influxdb.InfluxDBClient('10.0.12.127', 8086, 'admin', '123456', 'NOAA_water_dataabase')
#client = InfluxDBClient(host='mydomain.com', port=8086, username='myuser', password='mypass' ssl=True, verify_ssl=True)
#q = "select * from h2o_feet LIMIT 2"
#df = pd.DataFrame(client.query(q, chunked=True, chunk_size=10000).get_points())
client.query('SELECT * FROM h2o_feet LIMIT 2')
results.raw