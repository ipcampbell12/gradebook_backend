from db import db 

class StudentModel(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), unique=False, nullable=False)
    lname = db.Column(db.String(80), unique=False, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), unique=False, nullable=False)

    #one to many relationship with teachers (child)
    teacher = db.relationship("TeacherModel",back_populates="students")
    
    assessments = db.relationship("StudentsAssessments",back_populates="student")
    #Should that be "students" instead of "student"?

    # # one ot many relationship with grades (parent)
    # grades = db.relationship("GradeModel", back_populates="student", cascade="all,delete")

    

    