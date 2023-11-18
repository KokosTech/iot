from flask import url_for

def get_endpoints(app):
    endpoints = []
    for rule in app.url_map.iter_rules():
        endpoints.append({
            "url": rule.rule,
            "methods": list(rule.methods)
        })
    return endpoints

def get_sitemap(app):
    return {
        "url": url_for('index', _external=True),
        "endpoints": [
            get_endpoints(app)
        ]
    }
