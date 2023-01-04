from db import db 

class GradeModel(db.Model):
    __tablename__ = "grades"

    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer,db.ForeignKey("subjects.id"))
    grade = db.Column(db.Integer, nullable=False)

    students_assessments = db.relationship("StudentsAssessments",back_populates="grade", lazy="dynamic",cascade="all,delete")
