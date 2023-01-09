from flask import request
from flask_smorest import abort, Blueprint
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_jwt_extended import jwt_required
from sqlalchemy import func
import json


from db import db
from Models import AssessmentModel, TeacherModel, StudentModel, StudentsAssessments, SubjectModel
from schemas import AssessmentSchema, StudentAndAssessmentSchema, StudentSchema, SubjectSchema

#TeacherAndAssessmentSchema,

blp = Blueprint("Assessments",__name__,description="Operations on assessments")

@blp.route("/assessment/<string:assessment_id>")
class Assessment(MethodView):

    @jwt_required
    @blp.response(200,AssessmentSchema)
    def get(self,assessment_id):
        assessment = AssessmentModel.query.get_or_404(assessment_id)
        return assessment
    
    @jwt_required
    def delete(self, assessment_id):
        assessment = AssessmentModel.query.get_or_404(assessment_id)

        db.session.delete(assessment)
        db.session.commit()
        return {"message":f"The assessment {assessment.name} was deleted."}
    
    @jwt_required
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

    @jwt_required
    @blp.response(200,AssessmentSchema(many=True))
    def get(self):
        return AssessmentModel.query.all()

    @jwt_required
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
    
    @jwt_required
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

    @jwt_required
    @blp.response(200,StudentAndAssessmentSchema)
    def get(self,student_assessment_id):
        student_assessment = StudentsAssessments.query.get(student_assessment_id)

        return student_assessment

    @jwt_required
    def delete(self, student_assessment_id):
        student_assessment = StudentsAssessments.query.get(student_assessment_id)

        db.session.delete(student_assessment)
        db.session.commit()

        return {"message": "This student_assessment was deleted"}

    @jwt_required
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
    
    @jwt_required
    @blp.response(200,StudentAndAssessmentSchema(many=True))
    def get(self):
        students_assessments = db.session.query(StudentsAssessments).order_by(StudentsAssessments.student_id).all()
        return students_assessments


@blp.route("/grade/<string:student_id>")
class Scores(MethodView):

    @jwt_required
    def get(self,student_id):
        scores = db.session.query(StudentsAssessments.score).filter(StudentsAssessments.student_id == student_id).all()
        
        student = StudentModel.query.get_or_404(student_id)

        scores_list = [score["score"] for score in scores]
        
        average = round(sum(scores_list)/len(scores_list),1)

        return {"Student":f"{student.fname}{student.lname}","Overall Grade":average}

@blp.route("/score/<string:student_id>")
class ScoresList(MethodView):

    # @blp.response(200,StudentAndAssessmentSchema(many=True))
    @jwt_required
    def get(self,student_id):
        scores = db.session.query(StudentsAssessments.score, StudentsAssessments.assessment_id).filter(StudentsAssessments.student_id == student_id).all()
        
        tuple_scores = [dict(row) for row in scores]
        student = StudentModel.query.get_or_404(student_id)

        # json_scores = json.dumps(scores,default=str)

        return {"Student":f"{student.fname}{student.lname}","Scores":tuple_scores}
        

        
