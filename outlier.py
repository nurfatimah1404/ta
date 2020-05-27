import time
from datetime import datetime
from datetime import datetime
from influxdb import InfluxDBClient
import requests
import numpy

clientx = InfluxDBClient('10.0.12.127', 8086, 'admin', '123456', 'mydb')
clienty = InfluxDBClient('10.0.12.127', 8086, 'admin', '123456', 'hasilolah')
current_data = clientx.query("SELECT value FROM PM_10 where time<='2020-05-09 00:59:14'")
list_current_data = list(current_data.get_points())
#print(list_current_data)
elements = numpy.array(list_current_data['value'])
mean = numpy.mean(elements, axis=0)
sd = numpy.std(elements, axis=0)
final_listx = [x for x in list_current_data['value'] if (x > mean - 2 * sd)]
final_list = [x for x in final_listx if (x < mean + 2 * sd)]
print(final_list)

#arr = [10, 386, 479, 627, 20, 523, 482, 483, 542, 699, 535, 617, 577, 471, 615, 583, 441, 562, 563, 527, 453, 530, 433, 541, 585, 704, 443, 569, 430, 637, 331, 511, 552, 496, 484, 566, 554, 472, 335, 440, 579, 341, 545, 615, 548, 604, 439, 556, 442, 461, 624, 611, 444, 578, 405, 487, 490, 496, 398, 512, 422, 455, 449, 432, 607, 679, 434, 597, 639, 565, 415, 486, 668, 414, 665, 763, 557, 304, 404, 454, 689, 610, 483, 441, 657, 590, 492, 476, 437, 483, 529, 363, 711, 543]

