from flask import request
from flask_smorest import Blueprint,abort
from flask.views import MethodView
from schemas import TeacherSchema, LoginSchema
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt, create_refresh_token

from passlib.hash import pbkdf2_sha256

from db import db
from Models import TeacherModel
from instance.blocklist import BLOCKLIST
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("Teachers",__name__,description="Operations on teachers")

@blp.route('/teacher/<string:teacher_id>')
class Teacher(MethodView):

    # @jwt_required
    @blp.response(200,TeacherSchema)
    def get(self,teacher_id):
        teacher = TeacherModel.query.get_or_404(teacher_id)
        return teacher 

    # @jwt_required()
    def delete(self, teacher_id):
        teacher = TeacherModel.query.get_or_404(teacher_id)
        
        db.session.delete(teacher)
        db.session.commit()

        return {"message":f"The teacher {teacher.fname} was deleted "}
    
    # @jwt_required()
    @blp.arguments(TeacherSchema)
    @blp.response(200,TeacherSchema)
    def put(self, teacher_data, teacher_id):
        teacher = TeacherModel.query.get(teacher_id)

        if teacher:
            teacher.fname = teacher_data["fname"]
            teacher.lname = teacher_data["lname"]
        else:
            teacher = TeacherModel(id=teacher_id, **teacher_data)
        
        db.session.add(teacher)
        db.session.commit()

        return teacher


@blp.route('/teacher')
class TeachersList(MethodView):
    
    # @jwt_required()
    @blp.response(200,TeacherSchema(many=True))
    def get(self):
        return TeacherModel.query.all()
    
    @blp.arguments(TeacherSchema)
    @blp.response(200,TeacherSchema)
    def post(self, teacher_data):
        
        if TeacherModel.query.filter(TeacherModel.username == teacher_data["username"]).first():
            abort(409, message="A user with that username already exists")

        teacher = TeacherModel(
            fname= teacher_data["fname"],
            lname=teacher_data["lname"],
            username=teacher_data["username"],
            password=pbkdf2_sha256.hash(teacher_data["password"])
            )
       
        try: 
            db.session.add(teacher)
            print(teacher)
            db.session.commit()
            print("The teacher was created")
        except IntegrityError:
            abort(400, "A teacher with this name already exists")
            
        except SQLAlchemyError:
            print("There was a problem")
            abort(500, "There was an error when adding this teacher")
            

        return {"message":f"The teacher accoutn for {teacher} was created successfully"}, 201
    
@blp.route("/login")
class TeacherLoginClass(MethodView):
    @blp.arguments(LoginSchema)
    def post(self, teacher_data):

        teacher = TeacherModel.query.filter(TeacherModel.username == teacher_data["username"]).first()

        if teacher and pbkdf2_sha256.verify(teacher_data["password"], teacher.password):

            access_token = create_access_token(identity=teacher.id, fresh=True)

            refresh_token = create_refresh_token(identity=teacher.id)

            return{"access_token":access_token,"refresh_token":refresh_token}

        abort(401, message="Invalid credentials")

@blp.route("/logout")
class TeacherLogout(MethodView):
    
    # @jwt_required()
    def post(self):
        jti=get_jwt()["jti"]
        BLOCKLIST.add(jti)
       

        return {"message":"User successfully logged out."}


@blp.route("/refresh")
class TokenRefresh(MethodView):

    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)

        return {"access_token":new_token}
