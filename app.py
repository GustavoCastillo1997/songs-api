from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import all_blueprints



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:Katoreborn1611*mysql@localhost:3306/streaming'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

for bp in all_blueprints:
    app.register_blueprint(bp)

db = SQLAlchemy(app)
