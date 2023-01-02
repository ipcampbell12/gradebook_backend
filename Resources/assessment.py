from flask import request
from flask_smorest import abort, Blueprint
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


from db import db
from Models import AssessmentModel
from schemas import AssessmentSchema

blp = Blueprint("Assessments",__name__,description="Operations on assessments")

@blp.route("/assessments/<string:assessment_id>")
class Assessment(MethodView):
    def get(self,assessment_id):
        assessment = AssessmentModel.query.get_or_404(assessment_id)
        return assessment

class AsessmentList(MethodView):
    def post(self,assessment_data):

        assessment = AssessmentModel(**assessment_data)

        try:
            db.session.add(assessment)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, "We could not add this assessment")

        return assessment

