import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from influxdb import InfluxDBClient
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.graphics.tsaplots import plot_acf
from scipy.stats import linregress
client = InfluxDBClient('10.0.12.127', 8086)
h2O = client.query('SELECT mean("degrees") AS "h2O_temp" FROM "NOAA_water_database"."autogen"."h2o_temperature"  GROUP BY time(12h) LIMIT 60')
h2O_points = [p for p in h2O.get_points()]
h2O_df = pd.DataFrame(h2O_points)
h2O_df['time_step'] = range(0,len(h2O_df['time']))
h2O_df.plot(kind='line',x='time_step',y='h2O_temp')
plt.show()
print(h2O)