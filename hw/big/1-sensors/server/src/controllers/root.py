from flask import jsonify

from __main__ import app
from services.sitemap import get_sitemap


@app.route('/', methods=['GET'])
def index():
    return jsonify(get_sitemap(app))
