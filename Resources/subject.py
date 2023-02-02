from flask import request
from flask_smorest import abort, Blueprint
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_jwt_extended import jwt_required


from db import db
from Models import SubjectModel, TeacherModel
from schemas import SubjectSchema

blp = Blueprint("SubjectModel",__name__,description="Operations on subjects")

@blp.route("/subject/<string:subject_id>")
class Subject(MethodView):

    # @jwt_required()
    @blp.response(200, SubjectSchema)
    def get(self,subject_id):
        subject = SubjectModel.query.get_or_404(subject_id)
        return subject
    
    # @jwt_required()
    def delete(self, subject_id):
        subject = SubjectModel.query.get_or_404(subject_id)

        db.session.delete(subject)
        db.session.commit()
        return {"message":f"The subject {subject.name} was deleted."}
    
    # @jwt_required()
    @blp.arguments(SubjectSchema)
    @blp.response(200,SubjectSchema)
    def put(self, subject_data, subject_id):
        subject = SubjectModel.query.get(subject_id)

        if subject:
            subject.name = subject_data["name"]
        else:
            subject = SubjectModel(id=subject_id, **subject_data)
        
        db.session.add(subject)
        db.session.commit()

        return subject

@blp.route("/subject/<string:teacher_id>")
class SubjectList(MethodView):

    # @jwt_required()
    @blp.response(200,SubjectSchema(many=True))
    def get(self,teacher_id):
        return SubjectModel.join(TeacherModel, SubjectModel.teacher_id == TeacherModel.id).filter(TeacherModel.id ==teacher_id).query.all()
    
    # @jwt_required()
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
