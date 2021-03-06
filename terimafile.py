
from flask import Flask, request, redirect, url_for, jsonify, render_template, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
import os
# For Random
import random
# from gpiozero import CPUTemperature
from influxdb import InfluxDBClient
from influxdb import DataFrameClient
from CounterData import getCounter, clearCounter
from config import influxDBName

UPLOAD_FOLDER = '/home/data/post'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__, template_folder="webdoc/templates",
            static_folder='webdoc/static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/getData')
def hello_world():
    
    # def gantiFormatWaktu(row):
    #     row['time'] = datetime.strptime(row['time'], '%Y-%m-%dT%H:%M:%S.%fZ')
    #     return row
    # @app.route('/ambildata')
    # def ambil_data():
    #     #query Influx
    # idSensor = request.args.get('id')
    # measurement = request.args.get('sensor')
    # print(measurement)
    # print(idSensor)

    clientx = InfluxDBClient('182.23.82.22', 8086, 'admin', '123456', 'mydb')
    query  = "SELECT * FROM temperature WHERE id='cd14'"
    data  = clientx.query(query)
    list_current_data = list(data.get_points())
    # print(list_current_data)
    # for row in list_current_data:
    #     row['time'] = datetime.strptime(row['time'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d %H:%M:%S.%f')
    #     dataKirim.append(row)
    return jsonify(list_current_data)

@app.route('/getAverage')
def getAverage():
    idSensor = request.args.get('id')
    measurement = request.args.get('sensor')
    clientx = InfluxDBClient('182.23.82.22', 8086, 'admin', '123456', influxDBName())
    nowString = datetime.now().strftime("%Y-%m-%d")
    pastString = (datetime.now() + timedelta(days=-30)).strftime("%Y-%m-%d")
    query  = "SELECT MEAN(value) FROM {} where id='{}' AND time >='{} 00:00:00' AND time <='{} 23:00:00'group by time(1h)".format(measurement, idSensor, pastString, nowString)
    data  = clientx.query(query)
    list_current_data = list(data.get_points())
    return jsonify(list_current_data)

@app.route('/getAverageRahmad')
def getAverageRahmad():
    idSensor2 = request.args.get('id')
    measurement2 = request.args.get('sensor')
    clientx2 = InfluxDBClient('182.23.82.22', 8086, 'admin', '123456', influxDBName())
    query2  = "SELECT MEAN(value) FROM {} where id='{}' AND time >='2020-09-15 07:20:00' AND time <='2020-09-15 20:00:00' group by time(1h)".format(measurement2, idSensor2)
    data2  = clientx2.query(query2)
    list_current_data2 = list(data2.get_points())
    # print(list_current_data2)
    return jsonify(list_current_data2)

# @app.route('/getRahmad')
# def getRahmad():
#     idSensor2 = request.args.get('id')
#     measurement2 = request.args.get('sensor')
#     latitude2 = request.args.get('latitude')
#     longitude2 = request.args.get('longitude')
#     clientx2 = InfluxDBClient('182.23.82.22', 8086, 'admin', '123456', influxDBName())
#     query2  = "SELECT value FROM {} where id='{}' AND latitude = {} OR longitude={}  ".format(measurement2, idSensor2, latitude2, longitude2)
#     data2  = clientx2.query(query2)
#     list_current_data2 = list(data2.get_points())
#     # print(list_current_data2)
#     return jsonify(list_current_data2)

@app.route('/getRahmadtes')
def getRahmadtes():
    idSensor2 = request.args.get('id')
    measurement2 = request.args.get('sensor')
    latitude2 = request.args.get('latitude')
    longitude2 = request.args.get('longitude')
    time1  = request.args.get('time1')
    time2 = request.args.get('time2')
    # groupby = request.args.get('groupby')
    clientx2 = InfluxDBClient('182.23.82.22', 8086, 'admin', '123456', influxDBName())
    query2  = "SELECT mean(value) FROM {} where id='{}' AND latitude = {} OR longitude={} AND time >='{}' AND time <='{}' group by time(20m) ".format(measurement2, idSensor2, latitude2, longitude2, time1, time2)
    data2  = clientx2.query(query2)
    list_current_data2 = list(data2.get_points())
    # print(list_current_data2)
    return jsonify(list_current_data2)

@app.route('/getFau')
def getFau():
    clientx3 = InfluxDBClient('182.23.82.22', 8086, 'admin', '123456', influxDBName())
    # query3  = "SELECT * FROM {} where id='{}' ".format(measurement3, idSensor3)
    tanggal1 = request.args.get('tanggal')
    now = datetime.strptime(tanggal1,"%Y-%m-%d")
    tanggal2 = (now + timedelta(days=+1)).strftime("%Y-%m-%d")
    query  = "SELECT * FROM pm10 where id='3F0D' OR id='C7CD' OR id='25DC' AND time >='{}' AND time <'{}'".format(tanggal1, tanggal2)
    data  = clientx3.query(query)
    listData = list(data.get_points())
    dataResult = []
    for row in listData:
        # time = datetime.strptime(row['time'], '%Y-%m-%dT%H:%M:%S.%f000Z')
        if row['longitude'] is None:
            continue
        # Ambil CO
        queryCO = "SELECT * FROM co where id='3F0D' OR id='C7CD' AND time = '{}' AND latitude = {} AND longitude = {}".format(row['time'], row['latitude'], row['longitude'])
        dataCO  = clientx3.query(queryCO)
        dataCO = list(dataCO.get_points())
        # Ambil Temperature
        queryTemp = "SELECT * FROM temperature where id='3F0D' OR id='C7CD' AND time = '{}' AND latitude = {} AND longitude = {}".format(row['time'], row['latitude'], row['longitude'])
        dataTemp  = clientx3.query(queryTemp)
        dataTemp = list(dataTemp.get_points())
        # Ambil Humidity
        queryHum = "SELECT * FROM humidity where id='3F0D' OR id='C7CD' AND time = '{}' AND latitude = {} AND longitude = {}".format(row['time'], row['latitude'], row['longitude'])
        dataHum  = clientx3.query(queryHum)
        dataHum = list(dataHum.get_points())
        # Ambil CO2
        queryCO2 = "SELECT * FROM co2 where id='3F0D' OR id='C7CD' AND time = '{}' AND latitude = {} AND longitude = {}".format(row['time'], row['latitude'], row['longitude'])
        dataCO2  = clientx3.query(queryCO2)
        dataCO2 = list(dataCO2.get_points())
        # Susun Data
        dataResult.append({
            'time' : row['time'],
            'latitude' : row['latitude'],
            'longitude' : row['longitude'],
            'pm10' : row['value'],
            'temperature' : 0 if len(dataTemp) == 0 else dataTemp[0]['value'],
            'co' : 0 if len(dataCO) == 0 else dataCO[0]['value'],
            'humidity' : 0 if len(dataHum) == 0 else dataHum[0]['value'],
            'co2' : 0 if len(dataCO2) == 0 else dataCO2[0]['value']
        })
    return jsonify(dataResult)
    # return(tanggal1)


@app.route('/')
def tampilkanData():
    return render_template("welcome.html")


@app.route('/api', methods=['POST'])
def getFiles():
    # Check if file not exist in POST request
    if 'file' not in request.files:
        return jsonify({'response': 'error', 'message': 'Field file not found!'})
    file = request.files['file']
    # Check if filename is empty
    if file.filename == '':
        return jsonify({'response': 'error', 'message': 'Filename is empty!'})
    # Check if file is allowed extension
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'response': 'success', 'message': 'Upload success!'})
    else:
        return jsonify({'response': 'error', 'message': 'File extension denied!'})

@app.route('/<path:filename>')
def custom_static(filename):
    return send_from_directory('./webdoc/static/', filename)

@app.route('/getCounter', methods=['GET'])
def counter():
    date = request.args.get("date")
    return jsonify(getCounter(date))

@app.route('/clearCounter', methods=['GET'])
def clear():
    clearCounter()
    return redirect('/')

app.run('182.23.82.22', 8000, debug=True)
