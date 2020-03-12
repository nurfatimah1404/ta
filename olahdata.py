import influxdb
dfclient = influxdb.DataFrameClient('10.0.12.127', 8086, 'admin', '123456', 'NOAA_water_dataabase')
q = "select * from h2o_feet"
df = dfclient.query(q, chunked=True)  # Returns only 10k points