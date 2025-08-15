from flask import Flask
from db import db
from routes import all_blueprints
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

for bp in all_blueprints:
    app.register_blueprint(bp, url_prefix='/api')

@app.route('/')
def index():
    output = ["📚 Available API Endpoints:\n"]

    for rule in app.url_map.iter_rules():
        if rule.endpoint == 'static':
            continue

        methods = ', '.join(sorted(rule.methods - {'HEAD', 'OPTIONS'}))
        line = f"{methods:15} {rule.rule}"
        output.append(line)

    return "<pre>" + "\n".join(output) + "</pre>"

if __name__ == '__main__':
    debug_mode = app.config.get("DEBUG", False)
    app.run(debug=debug_mode)
    app.run(debug=True)
