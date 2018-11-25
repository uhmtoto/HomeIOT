from flask_sqlalchemy import SQLAlchemy
from iot import db

class Schedule(db.Model):
    __table_name__ = 'Schedule'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer, nullable=False)
    room = db.Column(db.String, nullable=False)
    temp = db.Column(db.Integer, nullable=False)
    # temp = 0 => off
    # temp > 0 => temp

    def __repr__(self):
        return f"{self.time}"

db.create_all()
