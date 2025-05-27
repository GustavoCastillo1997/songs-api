from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db import db
from routes import all_blueprints


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:Katoreborn1611*mysql@localhost:3306/streaming'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Registra os blueprints
for bp in all_blueprints:
    app.register_blueprint(bp)

@app.route('/')
def index():
    return "API funcionando! 🚀"

# Rodar app
if __name__ == '__main__':
    app.run(debug=True)
