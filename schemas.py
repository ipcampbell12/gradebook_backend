from marshmallow import Schema, fields

class PlainTeacherSchema(Schema):
    id = fields.Str(dump_only=True)
    fname = fields.Str(required=True)
    lname = fields.Str(required=True)

class PlainStudentSchema(Schema):
    id = fields.Str(dump_only=True)
    fname = fields.Str(required=True)
    lname = fields.Str(required=True)

class PlainAssessmentSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    date = fields.DateTime(required=True)

class PlainSubjectSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class StudentSchema(PlainStudentSchema):
    teacher_id = fields.Int(required=True, load_only=True)
    teacher = fields.Nested(PlainTeacherSchema(),dump_only=True)

class TeacherSchema(PlainTeacherSchema):
    students = fields.List(fields.Nested(PlainStudentSchema()),dump_only=True)

class AssessmentSchema(PlainAssessmentSchema):
    subject_id=fields.Int(required=True,load_only=True)
    subject = fields.Nested(PlainSubjectSchema(),dump_only=True)

class SubjectSchema(PlainSubjectSchema):
    assessments = fields.List(fields.Nested(PlainAssessmentSchema(),dump_only=True))

#primary keys are dump only, and foreign keys are load only