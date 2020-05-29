import time
from datetime import datetime
from datetime import datetime
from influxdb import InfluxDBClient
import requests
import numpy
# identify outliers with standard deviation
#from numpy.random import seed
#from numpy.random import randn
from numpy import mean
from numpy import std

clientx = InfluxDBClient('10.0.12.127', 8086, 'admin', '123456', 'mydb')
clienty = InfluxDBClient('10.0.12.127', 8086, 'admin', '123456', 'hasilolah')
current_data = clientx.query("SELECT value FROM PM_10 where time<='2020-05-09 00:59:14'")
list_current_data = list(current_data.get_points())
#print(list_current_data)
data = list_current_data['value']
# calculate summary statistics
data_mean, data_std = mean(data), std(data)
# identify outliers
cut_off = data_std * 3
lower, upper = data_mean - cut_off, data_mean + cut_off
# identify outliers
outliers = [x for x in data if x < lower or x > upper]
print(outliers)
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))
print(outliers_removed)