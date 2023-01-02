from flask import request
from flask_smorest import abort, Blueprint
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


from db import db
from Models import SubjectModel
from schemas import SubjectSchema

blp = Blueprint("SubjectModel",__name__,description="Operations on subjects")

@blp.route("/subject/<string:subjuect_id>")
class Subject(MethodView):

    @blp.response(200, SubjectSchema)
    def get(self,assessment_id):
        assessment = SubjectModel.query.get_or_404(assessment_id)
        return assessment

class SubjectList(MethodView):

    @blp.arguments(SubjectSchema)
    @blp.response(200, SubjectSchema)
    def post(self,assessment_data):

        assessment = SubjectModel(**assessment_data)

        try:
            db.session.add(assessment)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, "We could not add this assessment")

        return assessment
