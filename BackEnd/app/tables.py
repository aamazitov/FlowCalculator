from app import db
from datetime import datetime


class Calculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    calc_date = db.Column(db.DateTime, default=datetime.utcnow())
    radius = db.relationship("Radius", backref="calc", lazy="dynamic")
    time = db.relationship("Time", backref="calc", lazy="dynamic")


class Radius(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float(20), nullable=False)
    calc_id = db.Column(db.Integer, db.ForeignKey("calculation.id", ondelete="CASCADE"))
    pressure = db.relationship("Pressure", backref="radius", lazy="dynamic")
    temperature = db.relationship("Temperature", backref="radius", lazy="dynamic")


class Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float(20), nullable=False)
    calc_id = db.Column(db.Integer, db.ForeignKey("calculation.id", ondelete="CASCADE"))
    pressure = db.relationship("Pressure", backref="time", lazy="dynamic")
    temperature = db.relationship("Temperature", backref="time", lazy="dynamic")


class Pressure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float(20), nullable=False)
    radius_id = db.Column(db.Integer, db.ForeignKey("radius.id", ondelete="CASCADE"))
    time_id = db.Column(db.Integer, db.ForeignKey("time.id", ondelete="CASCADE"))


class Temperature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float(20), nullable=False)
    radius_id = db.Column(db.Integer, db.ForeignKey("radius.id", ondelete="CASCADE"))
    time_id = db.Column(db.Integer, db.ForeignKey("time.id", ondelete="CASCADE"))
