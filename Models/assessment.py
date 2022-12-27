from db import db
from datetime import datetime


class Assessment(db.Model):
    __tablename__ = 'assessments'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))