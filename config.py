import json


def influxServer():
    config = open('./config/config.json', 'r')
    config = json.load(config)
    return bool(config['influxServer'])

def influxDBName():
    config = open('./config/config.json', 'r')
    config = json.load(config)
    return bool(config['influxDBName'])