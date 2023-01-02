from db import db 

class StudentModel(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), unique=False, nullable=False)
    lname = db.Column(db.String(80), unique=False, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), unique=False, nullable=False)

    teacher = db.relationship("TeacherModel",back_populates="students")
    # assessments = db.relationship('Assessment', secondary=student_assessment, backref=db.backref(
    #     'students', cascade="all, delete-orphan", single_parent=True))
    