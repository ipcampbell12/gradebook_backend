from db import db 

class GradeModel(db.Model):
    __tablename__ = "grades"

    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer,db.ForeignKey("subjects.id"))
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"))

    #an aggregatation of all the students_assessments
    #but not a relationship column, so it cant be used for back_pouplates
    grade = db.Column(db.Integer, nullable=False)

    #one to many relationship with subjects (child)
    subject = db.relationship("SubjectModel",back_populates="grades")

    #one to many relationship with students (child)
    student = db.relationship("StudentModel",back_populates="grades")

    #one to many relationship with students_assssments (parent)
    students_assessments = db.relationship("StudentsAssessments",back_populates="grade", lazy="dynamic",cascade="all,delete")

   