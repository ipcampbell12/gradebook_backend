from marshmallow import Schema, fields

class TeacherSchema(Schema):
    id = fields.Str(dump_only=True)
    fname = fields.Str(required=True)
    lname = fields.Str(required=True)

