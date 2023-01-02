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
        raise NotImplementedError("Deleting a teacher has not been implemented yet")


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
 
