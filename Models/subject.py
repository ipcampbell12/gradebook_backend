from db import db 

class SubjectModel(db.Model):
    __tablename__ = 'subjects'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    assessments = db.relationship("AssessmentModel",back_populates="subject",lazy="dynamic")

    