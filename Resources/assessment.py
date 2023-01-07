from flask import request
from flask_smorest import abort, Blueprint
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy import func
import json


from db import db
from Models import AssessmentModel, TeacherModel, StudentModel, StudentsAssessments, SubjectModel
from schemas import AssessmentSchema, StudentAndAssessmentSchema, StudentSchema, SubjectSchema

#TeacherAndAssessmentSchema,

blp = Blueprint("Assessments",__name__,description="Operations on assessments")

@blp.route("/assessment/<string:assessment_id>")
class Assessment(MethodView):

    @blp.response(200,AssessmentSchema)
    def get(self,assessment_id):
        assessment = AssessmentModel.query.get_or_404(assessment_id)
        return assessment
    
    def delete(self, assessment_id):
        assessment = AssessmentModel.query.get_or_404(assessment_id)

        db.session.delete(assessment)
        db.session.commit()
        return {"message":f"The assessment {assessment.name} was deleted."}
    
    @blp.arguments(AssessmentSchema)
    @blp.response(200,AssessmentSchema)
    def put(self, assessment_data, assessment_id):
        assessment = AssessmentModel.query.get(assessment_id)

        if assessment:
            assessment.name = assessment_data["name"]
            assessment.subject_id = assessment_data["subject_id"]
        else:
            assessment = AssessmentModel(id=assessment_id, **assessment_data)
        
        db.session.add(assessment)
        db.session.commit()

        return assessment

@blp.route("/assessment")
class AsessmentList(MethodView):

    @blp.response(200,AssessmentSchema(many=True))
    def get(self):
        return AssessmentModel.query.all()

    @blp.arguments(AssessmentSchema)
    @blp.response(200,AssessmentSchema)
    def post(self,assessment_data):

        assessment = AssessmentModel(**assessment_data)

        try:
            db.session.add(assessment)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, "We could not add this assessment")

        return assessment
    

#add an assessment to a teachers 
# @blp.route("/teacher/<string:teacher_id>/assessment/<string:assessment_id>")
# class AddAssessmentToTeacher(MethodView):
    
#     @blp.response(201, AssessmentSchema)
#     def post(self, teacher_id, assessment_id):
#         teacher = TeacherModel.query.get_or_404(teacher_id)
#         assessment = AssessmentModel.query.get_or_404(assessment_id)
        

#         teacher.assessments.append(assessment)


#         try:
#             db.session.add(teacher)
#             db.session.commit()
#         except:
#             abort(500, message="An error occurred when inserting the tag")
        
#         return assessment


#add an assessment to a students 
@blp.route("/student/<string:student_id>/assessment/<string:assessment_id>")
class AddAssessmentToStudent(MethodView):
    
    @blp.arguments(StudentAndAssessmentSchema)
    @blp.response(201, AssessmentSchema)
    @blp.response(201, StudentSchema)
    def post(self, data, student_id, assessment_id):

        student = StudentModel.query.get(student_id)
        student_assessment = StudentsAssessments(score = data["score"])
        student_assessment.assessment = AssessmentModel.query.get(assessment_id)

        #print(type(assessment))
        #this is where it breaks 
        student.assessments.append(student_assessment)


        db.session.add(student_assessment)
        db.session.commit()
    
        
        return student_assessment
    

@blp.route("/student_assessment/<string:student_assessment_id>")
class StudentAssessmentList(MethodView):

    @blp.response(200,StudentAndAssessmentSchema)
    def get(self,student_assessment_id):
        student_assessment = StudentsAssessments.query.get(student_assessment_id)

        return student_assessment

    def delete(self, student_assessment_id):
        student_assessment = StudentsAssessments.query.get(student_assessment_id)

        db.session.delete(student_assessment)
        db.session.commit()

        return {"message": "This student_assessment was deleted"}

    @blp.arguments(StudentAndAssessmentSchema)
    @blp.response(200,StudentAndAssessmentSchema)
    def put(self,data, student_assessment_id):
        student_assessment = StudentsAssessments.query.get(student_assessment_id)

        if student_assessment:
            student_assessment.score = data["score"]
        
        db.session.add(student_assessment)
        db.session.commit()

        return student_assessment

@blp.route("/student_assessment")
class OtherStudentAssessmentList(MethodView):
    
    @blp.response(200,StudentAndAssessmentSchema(many=True))
    def get(self):
        students_assessments = db.session.query(StudentsAssessments).order_by(StudentsAssessments.student_id).all()
        return students_assessments


@blp.route("/grade/<string:student_id>")
class Scores(MethodView):

    def get(self,student_id):
        scores = db.session.query(StudentsAssessments.score).filter(StudentsAssessments.student_id == student_id).all()
        
        scores_list = [score["score"] for score in scores]
        

        average =sum(scores_list)/len(scores_list)

        print(average)
        print(scores_list)
        return {"Grade":average}
        

        
