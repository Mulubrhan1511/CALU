from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://calu_user:password@localhost/calu_db'
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['UPLOAD_FOLDER'] = '/img'


db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50)) 
    major = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    study = db.Column(db.String(50))
    image = db.Column(db.LargeBinary)