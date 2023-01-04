from db import db
from datetime import date


class AssessmentModel(db.Model):
    __tablename__ = 'assessments'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    date = db.Column(db.DateTime, default=date)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'),unique=False, nullable=False)
    

    subject = db.relationship("SubjectModel",back_populates="assessments")
  
    teachers = db.relationship("TeacherModel",back_populates="assessments",secondary="teachers_assessments")

    students = db.relationship("StudentsAssessments",back_populates="assessment")
