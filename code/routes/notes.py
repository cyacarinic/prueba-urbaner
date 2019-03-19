# -*- coding: utf-8 -*-
import json
from bottle import abort
from bottle import get, post, request
from routes import auth_verify, parse_response
from schemas.note import NoteSchema
from models.note import Note


# Get list of Notes
@get('/notes', method=['OPTIONS', 'GET'])
def note_list():
    user_token = auth_verify(dict(request.headers))
    collection = []
    list_notes = Note.select().where(Note.owner_id == user_token["id"])
    for note in list_notes:
        owner = note.owner.to_dict()
        note = note.to_dict()
        note.update({"owner": owner})
        collection.append(note)
    return parse_response(collection)


# Save a new Note
@post('/notes')
def note_save():
    user_token = auth_verify(dict(request.headers))
    body = request.json
    body.update({
        "owner_id": user_token["id"]
    })
    validated = NoteSchema().load(body)

    if validated.errors:
        abort(400, validated.errors)

    noteData = Note(**validated.data)
    noteData.save()

    return parse_response(validated.data)
