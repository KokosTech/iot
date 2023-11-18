from flask import jsonify, request

from __main__ import app
from services.data import get_data_stat


@app.route('/stats', methods=['GET'])
def get_stats():
    if request.method != 'GET':
        return jsonify({'error': 'Method not allowed'}), 405

    stats = None

    try:
        stats = get_data_stat()
    except RuntimeError as e:
        if str(e) == 'No data found':
            return jsonify({'error': str(e)}), 404
        else:
            return jsonify({'error': str(e)}), 500

    return jsonify(stats), 200
