from db import db

class StudentsAssessments(db.Model):
    __tablename__ = "students_assessments"

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer,db.ForeignKey("students.id"))
    assessment_id = db.Column(db.Integer,db.ForeignKey("assessments.id"))
    score = db.Column(db.Integer, nullable=False, default=None)
    grade_id = db.Column(db.Integer, db.ForeignKey("grades.id"))

    #many to many with students
    assessment = db.relationship("AssessmentModel",back_populates="students")
    student = db.relationship("StudentModel",back_populates="assessments")

    #one to many with grades
    student_assessment = db.relationship("GradeModel",back_populates="students_assessments")
