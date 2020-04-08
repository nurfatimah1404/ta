import pandas as pd
#import influxdb
from influxdb import InfluxDBClient
#client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
dbhost = "10.0.12.127"
dbport = 8086
dbuser = "admin"
dbpassword = "123456"
dbname = "NOAA_water_database'"
dbclient = InfluxDBClient(dbhost, dbport, dbuser, dbpassword, dbname)
#client = InfluxDBClient('10.0.12.127', 8086, 'admin', '123456', 'NOAA_water_database')
#client = InfluxDBClient(host='mydomain.com', port=8086, username='myuser', password='mypass' ssl=True, verify_ssl=True)
q = "SELECT MEAN(water_level) FROM h2o_feet GROUP BY time(1h) LIMIT 8"
#SELECT MEAN("water_level") FROM "h2o_feet" GROUP BY "location"
df = pd.DataFrame(dbclient.query(q, chunked=True, chunk_size=10000).get_points())
print (df)
time = df.iloc[:,1]
mean = df.iloc[:,0]
#print(df.loc[[159220]])
json_body = [
            {
                "measurement": "olah_h2o",
                "time": time,
                "fields": {
                    "value" : mean
                } 
            }
        ]
dbclient.write_points(json_body)
print("Finished writing to InfluxDB")
print (json_body)