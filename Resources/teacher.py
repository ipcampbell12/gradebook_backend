from flask import request
from flask_smorest import Blueprint,abort
from flask.views import MethodView
from schemas import TeacherSchema

from db import db
from Models import TeacherModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("Teachers",__name__,description="Operations on teachers")

@blp.route('/teacher/<string:teacher_id>')
class Teacher(MethodView):

    @blp.response(200,TeacherSchema)
    def get(self,teacher_id):
        teacher = TeacherModel.query.get_or_404(teacher_id)
        return teacher 

    
    def delete(self, teacher_id):
        teacher = TeacherModel.query.get_or_404(teacher_id)
        
        db.session.delete(teacher)
        db.session.commit()

        return {"message":f"The teacher {teacher.fname} was deleted "}
    
    @blp.arguments(TeacherSchema)
    @blp.response(200,TeacherSchema)
    def put(self, teacher_data, teacher_id):
        teacher = TeacherModel.query.get(teacher_id)

        if teacher:
            teacher.fname = teacher_data["fname"]
            teacher.lname = teacher_data["lname"]
        else:
            teacher = TeacherModel(id=teacher_id, **teacher_data)
        
        db.session.add(teacher)
        db.session.commit()

        return teacher


@blp.route('/teacher')
class TeachersList(MethodView):
    
    @blp.response(200,TeacherSchema(many=True))
    def get(self):
        return TeacherModel.query.all()
    
    @blp.arguments(TeacherSchema)
    @blp.response(200,TeacherSchema)
    def post(self, teacher_data):
        
        teacher = TeacherModel(**teacher_data)

        try: 
            db.session.add(teacher)
            db.session.commit()
        except IntegrityError:
            abort(400, "A teacher with this name already exists")
        except SQLAlchemyError:
            abort(500, "There was an error when adding this teacher")

        return teacher, 201
 
