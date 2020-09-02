import sqlite3
from datetime import datetime
import os
import logging


class SqlMonitor:

    # Make directory for data now
    @staticmethod
    def createDir():
        try:
            os.makedirs("./db")
        except:
            pass

    # Write to SQL
    @staticmethod
    def sqlWrite(topic, data, receivedTime):
        # Login
        # logging.basicConfig(filename='./log/sqlite.log',
        #                     format='%(asctime)s %(message)s', level=logging.DEBUG)
        # try:
        SqlMonitor.createDir()
        delimiter = data.split(',')
        sensorDate = datetime.strptime(
        delimiter[0], "%Y-%m-%d %H:%M:%S.%f")

        conn = sqlite3.connect(
            './db/{}-{}-{}.db'.format(sensorDate.year, sensorDate.month, sensorDate.day))
        c = conn.cursor()
        # Create table
        c.execute("CREATE TABLE IF NOT EXISTS '%s' (sensorTime text NULL, receivedTime text NULL, id, value, lat NULL, long NULL)" % topic)
        item = (delimiter[0], receivedTime, delimiter[4], delimiter[1], delimiter[2], delimiter[3])
        c.execute("INSERT INTO '%s' values (?, ?, ?, ?, ?, ?)" %
                topic, item)
        conn.commit()
        conn.close()
        # except:
        #     # logging.exception("Error at writing db sql")
        #     pass

    # @staticmethod
    # def getQuery(stringQuery):
    #     conn = sqlite3.connect('./db/2020-8.db')
    #     c = conn.cursor()
    #     data = []
    #     for row in c.execute(stringQuery):
    #         time, value = row
    #         data.append({'time':time, 'value':value})
    #     conn.close()
    #     return data

# SqlMonitor.createDir()
# topic = 'co2'
# conn = sqlite3.connect('./db/abu.db')
# c = conn.cursor()
# # Create table
# c.execute("CREATE TABLE IF NOT EXISTS '%s' (date text NULL, trans text, symbol text, qty real, price real)" % topic)
# c.execute("INSERT INTO '%s' VALUES ('2006-01-05','BUY','RHAT',100,35.14)" % topic)
# conn.commit()
# conn.close()