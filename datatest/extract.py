import sqlite3
from datetime import datetime

# From


def getDelayTerima():
    conn = sqlite3.connect('db/a.db')
    c = conn.cursor()

    data = []
    for row in c.execute('SELECT * FROM data'):
        if row[2] != '':
            receiveTime = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S.%f')
            sendTime = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S.%f')
            duration = receiveTime - sendTime
            execution_time = duration.total_seconds() * 1000
            data.append(execution_time)

    print('Max = ' + str(max(data)))
    print('Min = ' + str(min(data)))
    print('Average = ' + str(sum(data) / len(data)))


def getDelayKirim():
    conn = sqlite3.connect('db/b.db')
    conn2 = sqlite3.connect('db/a.db')
    c = conn.cursor()
    c2 = conn2.cursor()
    data = []
    for row in c.execute('SELECT * FROM data'):
        c2.execute(
            'SELECT * FROM data WHERE sensorTime="{}" AND id="{}" AND topic="{}"'.format(row[0], row[3], row[2]))
        dataC2 = c2.fetchone()
        if dataC2 is None:
            continue
        sendTimeBS = datetime.strptime(dataC2[3], '%Y-%m-%d %H:%M:%S.%f')
        receiveTimeServer = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S.%f')
        duration =  sendTimeBS - receiveTimeServer
        execution_time = duration.total_seconds() * 1000
        data.append(execution_time)
    print('Max = ' + str(max(data)))
    print('Min = ' + str(min(data)))
    print('Average = ' + str(sum(data) / len(data)))


getDelayKirim()
print('------------')
getDelayTerima()
