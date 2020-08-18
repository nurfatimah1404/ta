
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
    idSensor = request.args.get('id')
    clientx = InfluxDBClient('10.0.12.127', 8086, 'admin', '123456', 'polusi')
    data  = clientx.query("SELECT * FROM temperature WHERE id='{}'".format(idSensor))
    list_current_data = list(data.get_points())
    dataKirim = []
    for row in list_current_data:
        row['time'] = datetime.strptime(row['time'], '%Y-%m-%dT%H:%M:%S.%9').strftime('%Y-%m-%d %H:%M:%S.%f')
        dataKirim.append(row)
    return jsonify(dataKirim)

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


app.run('10.0.12.127', 8000, debug=True)
