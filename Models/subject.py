from db import db 

class SubjectModel(db.Model):
    __tablename__ = 'subjects'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    #one to many relationship with assessments (parent)
    assessments = db.relationship("AssessmentModel",back_populates="subject",lazy="dynamic")

    #one to many relationship with assessments (parent)
    #THIS DOESN'T WORK BECASE BACK_POPULATES REFERS TO A COLUMN ON THAT TABLE, AND ASSESSMENTMODEL DOESN'T HAVE THAT COLUMN
    #BUT IT ALSO DOESN'T WORK BECASE GRADES ISN'T A DB.RELATIONSHIP COLUMN, IT'S JUST AN INTEGER COLUMNthere 
    # grades = db.relationship("GradeModel",back_populates="subject",lazy=True)

    