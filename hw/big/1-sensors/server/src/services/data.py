import matplotlib.pyplot as plt
import numpy as np

from io import BytesIO
import datetime
import base64

from __main__ import db


def get_data_by_id(id):
    return db.getById(id)

def get_data_by_device_id(device_id):
    return db.getBy({
        'device_id': device_id
    })

def get_data_by_device_id_and_timestamp(device_id, timestamp):
    return db.getBy({
        'device_id': device_id,
        'timestamp': timestamp
    })


def get_data_all():
    return db.getAll()


def add_data(
    value,
    timestamp,
    device_id
):
    try:
        value = float(value)
    except ValueError:
        raise ValueError('Invalid value provided')

    if value < 18 or value > 25:
        raise ValueError('Value out of range')

    try:
        timestamp = datetime.datetime.strptime(
            timestamp, '%Y-%m-%dT%H:%M:%S').isoformat()
    except ValueError:
        raise ValueError('Invalid timestamp provided')

    if not device_id or not isinstance(device_id, str) or len(device_id) == 0:
        raise ValueError('Invalid device_id provided')

    if get_data_by_device_id_and_timestamp(device_id, timestamp):
        raise ValueError('Duplicate data entry')

    return db.add({
        'value': value,
        'timestamp': timestamp,
        'device_id': device_id
    })


def get_stat_by_device_id(device_id):
    data = get_data_by_device_id(device_id)

    if not data:
        raise RuntimeError('No data found')

    return {
        'avg': np.average([x['value'] for x in data]),
        'min': np.min([x['value'] for x in data]),
        'max': np.max([x['value'] for x in data])
    }


def get_data_stat():
    data = get_data_all()

    if not data:
        raise RuntimeError('No data found')

    devices = {}

    for item in data:
        if item['device_id'] not in devices:
            devices[item['device_id']] = []

        devices[item['device_id']].append(item['value'])

    stats = {}

    for device_id in devices:
        entries = devices[device_id]
        print(entries)
        stats[device_id] = {
            'avg': np.average(entries),
            'min': np.min(entries),
            'max': np.max(entries)
        }

    return stats


def get_graph_by_device_id(device_id):
    data = get_data_by_device_id(device_id)

    if not data:
        raise RuntimeError('No data found')

    data = sorted(data, key=lambda x: x['timestamp'])

    plt.switch_backend('agg')
    plt.clf()

    plt.plot(
        [x['timestamp'] for x in data],
        [x['value'] for x in data]
    )

    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)

    # Return encoded image (graph) in base64
    return base64.b64encode(image_stream.getvalue()).decode('utf-8')
