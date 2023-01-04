from db import db

student_grades = db.Table(
    'student_grade',
    db.Column('student_id', db.Integer, db.ForeignKey("students.id")),
    db.Column("grade_id",db.Integer,db.ForeignKey("grades.id"))
)