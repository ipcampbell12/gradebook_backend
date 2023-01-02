from db import db   

student_assessment = db.Table(
    'student_assessment',
    db.Column('student_id',db.Integer,db.ForeignKey('students.id')),
    db.Column('assessment_id',db.Integer,db.ForeignKey('assessments.id'))
)