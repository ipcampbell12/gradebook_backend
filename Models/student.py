from db import db 

class StudentModel(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(80), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'),unique=True,nullable=False)
    # assessments = db.relationship('Assessment', secondary=student_assessment, backref=db.backref(
    #     'students', cascade="all, delete-orphan", single_parent=True))
    