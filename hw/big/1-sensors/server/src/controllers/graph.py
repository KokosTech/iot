from flask import jsonify, request, render_template

from __main__ import app
from services.data import get_stat_by_device_id, get_graph_by_device_id


@app.route('/graph/<device_id>', methods=['GET'])
def get_device_data(device_id):
    if request.method != 'GET':
        return jsonify({'error': 'Method not allowed'}), 405

    data = None
    graph = None

    try:
        data = get_stat_by_device_id(device_id)
        graph = get_graph_by_device_id(device_id)
    except RuntimeError as e:
        if str(e) == 'No data found':
            return jsonify({'error': str(e)}), 404
        else:
            return jsonify({'error': str(e)}), 500

    return render_template('graph.html', image=graph, data=data), 200
