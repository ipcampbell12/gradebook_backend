from marshmallow import Schema, fields

class TeacherSchema(Schema):
    # message = fields.Str()
    id = fields.Int(dump_only=True)
    fname = fields.Str(required=True)
    lname = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)

class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)

class PlainStudentSchema(Schema):
    id = fields.Int(dump_only=True)
    fname = fields.Str(required=True)
    lname = fields.Str(required=True)

class PlainAssessmentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    # date = fields.DateTime(required=True)

class PlainSubjectSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

# class PlainGradeSchema(Schema):
#     id = fields.Int(dump_only=True)
#     grade = fields.Int(required=True)

class StudentSchema(PlainStudentSchema):
    teacher_id = fields.Int(required=True, load_only=True)
    teacher = fields.Nested(TeacherSchema(),dump_only=True)
    assessments = fields.List(fields.Nested(PlainAssessmentSchema(),dump_only=True))
    # grades = fields.List(fields.Nested(PlainGradeSchema(),dump_only=True))
    
# class TeacherSchema(PlainTeacherSchema):
#     students = fields.List(fields.Nested(PlainStudentSchema()),dump_only=True)
    #assessments = fields.List(fields.Nested(PlainAssessmentSchema()),dump_only=True)

class AssessmentSchema(PlainAssessmentSchema):
    subject_id=fields.Int(required=True,load_only=True)
    subject = fields.Nested(PlainSubjectSchema(),dump_only=True)
    #students = fields.Nested(StudentSchema(),dump_only=True)

class SubjectSchema(PlainSubjectSchema):
    assessments = fields.List(fields.Nested(PlainAssessmentSchema(),dump_only=True))
    # grades = fields.List(fields.Nested(PlainSubjectSchema(),dump_only=True))


#the assessment/student id isn't returning anything because the api doesn't know what those are, since they aren't referencing any of the other schemas 

class StudentAndAssessmentSchema(Schema):
    # message = fields.Str()
    id = fields.Int(dump_only=True)
    assessment = fields.Nested(AssessmentSchema(only=("name",)),dump_only=True)
    score = fields.Int(required=True)
    student = fields.Nested(StudentSchema(only=("fname",)),dump_only=True)



# class TeacherAndAssessmentSchema(Schema):
#     message = fields.Str()∂
#     teacher = fields.Nested(TeacherSchema)
#     assessment = fields.Nested(AssessmentSchema)

# class GradeSchema(PlainGradeSchema):
#     student_id = fields.Int(required=True, load_only=True)
#     student = fields.Nested(PlainStudentSchema(),dump_only=True)
#     students_assessments = fields.List(fields.Nested(StudentAndAssessmentSchema(),dump_only=True))
#primary keys are dump only, and foreign keys are load only