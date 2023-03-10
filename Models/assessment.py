from db import db
from datetime import datetime


class AssessmentModel(db.Model):
    __tablename__ = 'assessments'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    # date = db.Column(db.DateTime, default=datetime.date)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'),unique=False, nullable=False)
    # scored= db.Column(db.Boolean, nullable=False, default=False )
    # possible = db.Column(db.Integer)
    # passing = db.Column(db.Integer)

    # one to many relationship with subject (child)
    subject = db.relationship("SubjectModel",back_populates="assessments")
  
    #many to many relationships students
    students = db.relationship("StudentsAssessments",back_populates="assessment",cascade="all,delete")


    # one to many relationship with teachers (child)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'),unique=False, nullable=False)
    teacher = db.relationship("TeacherModel",back_populates="assessments")
