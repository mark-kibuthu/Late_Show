# app.py
from flask import Flask
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Use SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()  # Create database tables

from routes import *

if __name__ == "__main__":
    app.run(debug=True, port=5555)
