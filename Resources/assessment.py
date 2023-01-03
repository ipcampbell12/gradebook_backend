from flask import request
from flask_smorest import abort, Blueprint
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


from db import db
from Models import AssessmentModel
from schemas import AssessmentSchema

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

