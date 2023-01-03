from db import db

class TeachersAssessments(db.Model):
    __tablename__ = "teachers_assessments"

    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"))
    assessment_id = db.Column(db.Integer, db.ForeignKey("assessments.id"))

