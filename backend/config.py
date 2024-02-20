from flask import Flask
from flast_sqlalchemy import SQLAlchemy
from flask_cors import CORS    #Cross origin requests

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)