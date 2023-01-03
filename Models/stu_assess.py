from db import db

class StudentsAssessments(db.Model):
    __tablename__ = "students_assessments"

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer,db.ForeignKey("students.id"))
    assessment_id = db.Column(db.Integer,db.ForeignKey("assessments.id"))
    score = db.Column(db.Integer, nullable=False)