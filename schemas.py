from marshmallow import Schema, fields

class PlainTeacherSchema(Schema):
    id = fields.Str(dump_only=True)
    fname = fields.Str(required=True)
    lname = fields.Str(required=True)

class PlainStudentSchema(Schema):
    id = fields.Str(dump_only=True)
    fname = fields.Str(required=True)
    lname = fields.Str(required=True)

class StudentSchema(PlainStudentSchema):
    teacher_id = fields.Int(required=True, load_only=True)
    teacher = fields.Nested(PlainTeacherSchema(),dump_only=True)

class TeacherSchema(PlainTeacherSchema):
    students = fields.List(fields.Nested(PlainStudentSchema()),dump_only=True)
