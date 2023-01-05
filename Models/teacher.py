from db import db 

class TeacherModel(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), unique=False, nullable=False)
    lname = db.Column(db.String(80), unique=False, nullable=False)

    #one to many relationship with students 
    students = db.relationship("StudentModel",back_populates="teacher",lazy="dynamic",cascade="all,delete")


    # assessments = db.relationship("AssessmentModel",back_populates="teachers",secondary="teachers_assessments")
    # email = db.Column(db.String(80), nullable=False)
    # password = db.Column(db.String(80), nullable=False)h

