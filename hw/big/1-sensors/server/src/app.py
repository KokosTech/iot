from flask import Flask

from db import db

app = Flask(__name__)

from controllers import root, data, graph, stats

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
