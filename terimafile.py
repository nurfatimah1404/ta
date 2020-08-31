
from flask import Flask, request, redirect, url_for, jsonify, render_template
from werkzeug.utils import secure_filename
from datetime import datetime
import os
# For Random
import random
# from gpiozero import CPUTemperature
from influxdb import InfluxDBClient
from influxdb import DataFrameClient

UPLOAD_FOLDER = '/home/data/post'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
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
    clientx = InfluxDBClient('182.23.82.22', 8086, 'admin', '123456', 'mydb')
    query  = "SELECT MEAN(value) FROM {} where id='{}' AND time >='2020-08-18 00:00:00' AND time <='2020-08-26 23:00:00'group by time(1h)".format(measurement, idSensor)
    data  = clientx.query(query)
    list_current_data = list(data.get_points())
    print(list_current_data)
    return jsonify(list_current_data)

@app.route('/getAverageRahmad')
def getAverageRahmad():
    idSensor2 = request.args.get('id')
    measurement2 = request.args.get('sensor')
    clientx2 = InfluxDBClient('182.23.82.22', 8086, 'admin', '123456', 'mydb')
    query2  = "SELECT MEAN(value) FROM {} where id='{}' AND time >='2020-08-25 09:00:00' AND time <='2020-08-25 13:49:19'group by time(1h)".format(measurement2, idSensor2)
    data2  = clientx2.query(query2)
    list_current_data2 = list(data2.get_points())
    print(list_current_data2)
    return jsonify(list_current_data2)

@app.route('/getFau')
def getFau():
    idSensor2 = request.args.get('id')
    measurement2 = request.args.get('sensor')
    clientx2 = InfluxDBClient('182.23.82.22', 8086, 'admin', '123456', 'mydb')
    query2  = "SELECT * FROM {} where id='{}' AND time >='2020-08-26 18:00:00' AND time <='2020-08-26 20:00s:19'group by time(1h)".format(measurement2, idSensor2)
    data2  = clientx2.query(query2)
    list_current_data2 = list(data2.get_points())
    print(list_current_data2)
    return jsonify(list_current_data2)

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


app.run('182.23.82.22', 8000, debug=True)
