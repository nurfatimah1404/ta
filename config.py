import json


def influxServer():
    config = open('./config/config.json', 'r')
    config = json.load(config)
    return bool(config['influxServer'])

def influxDBName():
    config = open('./config/config.json', 'r')
    config = json.load(config)
    return config['influxDBName']

def configTopic():
    config = open('./config/node.json', 'r')
    config = json.load(config)
    topic = []
    for node in config:
        for param in node['parameter']:
            topic.append((node['id']+'/'+param['name'], 0))
    return topic