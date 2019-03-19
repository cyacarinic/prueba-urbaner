# -*- coding: utf-8 -*-
from marshmallow import Schema, fields


class NoteSchema(Schema):
    owner_id = fields.Int()
    title = fields.Str(required=True)
    content = fields.Str(required=True)
