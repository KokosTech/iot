from flask import request, jsonify

from __main__ import app
from services.data import get_data_by_id, add_data


@app.route('/data', methods=['POST'])
def post_data():
    if request.method != 'POST':
        return jsonify({'error': 'Method not allowed'}), 405

    if not request.is_json:
        return jsonify({'error': 'Invalid content-type'}), 400

    dirty_data = request.get_json()

    if not dirty_data:
        return jsonify({'error': 'No data provided'}), 400

    if 'value' not in dirty_data:
        return jsonify({'error': 'No value provided'}), 400
    elif 'timestamp' not in dirty_data:
        return jsonify({'error': 'No timestamp provided'}), 400
    elif 'device_id' not in dirty_data:
        return jsonify({'error': 'No device_id provided'}), 400

    new_data = None

    try:
        new_data = get_data_by_id(add_data(
            dirty_data['value'],
            dirty_data['timestamp'],
            dirty_data['device_id']
        ))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    return jsonify(
        new_data
    ), 201
