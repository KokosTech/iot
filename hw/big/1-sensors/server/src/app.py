from db import db
from flask import Flask

app = Flask(__name__)

from controllers import data, graph, root, stats

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
