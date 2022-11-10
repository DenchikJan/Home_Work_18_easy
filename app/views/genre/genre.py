from flask import request
from flask_restx import Resource, Namespace

from app.database import db
from app.models import GenreSchema, Genres

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = db.session.query(Genres).all()
        response = genres_schema.dump(genres)

        return response, 200

    def post(self):
        req_json = request.json
        new_genre = Genres(**req_json)
        db.session.add(new_genre)
        db.session.commit()

        return "", 201


@genre_ns.route('/<int:git>')
class GenreView(Resource):
    def get(self, git: int):
        genre = db.session.query(Genres).filter(Genres.id == git).one()
        response = genre_schema.dump(genre)

        return response, 200

    def put(self, git: int):
        req_json = request.json
        genre = db.session.query(Genres).filter(Genres.id == git).one()

        genre.name = req_json.get('name')

        db.session.add(genre)
        db.session.commit()

        return "", 204

    def delete(self, did: int):
        genre = db.session.query(Genres).filter(Genres.id == did).one()

        db.session.delete(genre)
        db.session.commit()

        return "", 204
