# -*- coding: utf-8 -*-
from marshmallow import Schema, fields
from schemas.note import NoteSchema


class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    note = fields.Nested(NoteSchema())
