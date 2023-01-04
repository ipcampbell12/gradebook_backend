from db import db 

class StudentModel(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), unique=False, nullable=False)
    lname = db.Column(db.String(80), unique=False, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), unique=False, nullable=False)

    teacher = db.relationship("TeacherModel",back_populates="students")
    
    assessments = db.relationship("StudentsAssessments",back_populates="student")

    # def __init__(self,id,fname,lname,teacher_id,teacher,assessments):
    #     self.id = id 
    #     self.fname = fname
    #     self.lname = lname
    #     self.teacher_id = teacher_id
    #     self.teacher = teacher
    #     self.assessments = assessments

    