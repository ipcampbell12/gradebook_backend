from flask import request
from flask_smorest import abort, Blueprint
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


from db import db
from Models import SubjectModel
from schemas import SubjectSchema

blp = Blueprint("SubjectModel",__name__,description="Operations on subjects")

@blp.route("/subject/<string:subject_id>")
class Subject(MethodView):

    @blp.response(200, SubjectSchema)
    def get(self,subject_id):
        subject = SubjectModel.query.get_or_404(subject_id)
        return subject

@blp.route("/subject")
class SubjectList(MethodView):

    @blp.response(200,SubjectSchema(many=True))
    def get(self):
        return SubjectModel.query.all()
        
    @blp.arguments(SubjectSchema)
    @blp.response(200, SubjectSchema)
    def post(self,subject_data):

        subject = SubjectModel(**subject_data)

        try:

            db.session.add(subject)
            db.session.commit()
        except IntegrityError:
            abort(400, "A subject with this name already exists")
        except SQLAlchemyError:
            abort(500, "We could not add this subject")

        return subject
