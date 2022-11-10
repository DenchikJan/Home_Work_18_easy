from flask import request
from flask_restx import Resource, Namespace

from app.database import db
from app.models import DirectorSchema, Directors

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = db.session.query(Directors).all()
        response = directors_schema.dump(directors)

        return response, 201

    def post(self):
        req_json = request.json
        new_director = Directors(**req_json)
        db.session.add(new_director)
        db.session.commit()

        return "", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did: int):
        director = db.session.query(Directors).filter(Directors.id == did).one()
        response = director_schema.dump(director)

        return response, 201

    def put(self, did: int):
        req_json = request.json
        director = db.session.query(Directors).filter(Directors.id == did).one()

        director.name = req_json.get('name')

        db.session.add(director)
        db.session.commit()

        return "", 204

    def delete(self, did: int):
        director = db.session.query(Directors).filter(Directors.id == did).one()

        db.session.delete(director)
        db.session.commit()

        return "", 204
