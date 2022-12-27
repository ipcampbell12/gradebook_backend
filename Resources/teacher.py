from flask import request
from flask_smorest import Blueprint,abort
from flask.views import MethodView
from db import teachers
from schemas import TeacherSchema

blp = Blueprint("Teachers",__name__,description="Operations on teachers")

@blp.route('/teacher/<string:teacher_id>')
class Teacher(MethodView):

    def get(self,teacher_id):
        try:
            return teachers[teacher_id]
        except: 
            abort(404, message="Teacher not found")
    
    def delete(self, teacher_id):
        try:
            del teachers[teacher_id]
            return {"message":"Teacher deleted"}
        except KeyError: 
            abort(404,"Teacher not found")

@blp.rote('/teacher')
class TeachersList(MethodView):
    
    def get(self):
        return teachers.values()
    
    @blp.arguments(TeacherSchema)
    @blp.response(200,TeacherSchema)
    def post(self, teacher_data):
        
        teacher_id=teachers.values().length+1

        teacher = {**teacher_data,"id":teacher_id}
        teachers[teacher_id] = teacher 
        return teacher, 201
 
