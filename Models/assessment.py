from db import db
from datetime import datetime


class AssessmentModel(db.Model):
    __tablename__ = 'assessments'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'),unique=False, nullable=False)
    # teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'),unique=False, nullable=False)

    subject = db.relationship("SubjectModel",back_populates="assessments")
    # teacher = db.relationship("TeacherModel",back_populates="assessments")
