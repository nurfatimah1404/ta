from influxdb import DataFrameClient

client = DataFrameClient(host='10.0.12.127', port=8086, username='admin', password='123456', database='NOAA_water_database')
daata = "select * from h2o_feet where time > now() - 1h"
select * from h2o_feet where time > now() - 1h