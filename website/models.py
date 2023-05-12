from . import db

from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    commissions = db.relationship('Commission')

class Commission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    status = db.Column(db.String(20))
    price = db.Column(db.Integer)
    # image
    description = db.Column(db.String(100))
    commissioner = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment = db.Column(db.String(200))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

