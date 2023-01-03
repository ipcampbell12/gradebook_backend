from flask import request
from flask_smorest import Blueprint,abort
from flask.views import MethodView
from schemas import StudentSchema

from db import db
from Models import StudentModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("Students",__name__,description="Operations on students")

@blp.route("/student/<string:student_id>")
class Student(MethodView):

    @blp.response(200,StudentSchema)
    def get(self, student_id):
        student = StudentModel.query.get_or_404(student_id)
        return student 

    def delete(self, student_id):
        student = StudentModel.query.get_or_404(student_id)

        db.session.delete(student)
        db.session.commit()
        return {"message":f"The student {student.fname} was deleted."}
    
    @blp.arguments(StudentSchema)
    @blp.response(200,StudentSchema)
    def put(self, student_data, student_id):
        student = StudentModel.query.get(student_id)

        if student:
            student.fname = student_data["fname"]
            student.lname = student_data["lname"]
            student.teacher_id = student_data["teacher_id"]
        else:
            student = StudentModel(id=student_id, **student_data)
        
        db.session.add(student)
        db.session.commit()

        return student


@blp.route('/student')
class StudentList(MethodView):
    
    @blp.response(200,StudentSchema(many=True))
    def get(self):
        return StudentModel.query.all()

    @blp.arguments(StudentSchema)
    @blp.response(200,StudentSchema)
    def post(self,student_data):

        student = StudentModel(**student_data)

        try:
            db.session.add(student)
            db.session.commit()
            
        except SQLAlchemyError:
            abort(500, "There was an error adding this student")
        

        return student