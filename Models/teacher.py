from db import db 

class TeacherModel(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(80), nullable=False)
    # email = db.Column(db.String(80), nullable=False)
    # password = db.Column(db.String(80), nullable=False)

    # def __init__(self,fname,lname):
    #     self.fname = fname 
    #     self.lname = lname 
    
    # def json(self):
    #     return {'fname':self.fname, 'lname':self.lname}

    # @classmethod
    # def find_by_id(cls,id):
    #     return cls.query.filter_by(id=id).first()


    # def save_to_db(self):
    #     db.session.add(self)
    #     db.session.commit()

    # def delete_from_db(self):
    #     db.session.delete(self)
    #     db.session.commit()
