from flask import request
from flask_restx import Resource, Namespace

from app.database import db
from app.models import MovieSchema, Movies

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        if request.args.get('year'):
            year = request.args.get('director_id')
            director_movies = db.session.query(Movies).filter(Movies.year == year)
            response = movies_schema.dump(director_movies)

            return response, 201

        elif request.args.get('director_id'):
            director_id = request.args.get('director_id')
            director_movies = db.session.query(Movies).filter(Movies.director_id == director_id)
            response = movies_schema.dump(director_movies)

            return response, 201

        elif request.args.get('genre_id'):
            genre_id = request.args.get('genre_id')
            director_movies = db.session.query(Movies).filter(Movies.genre_id == genre_id)
            response = movies_schema.dump(director_movies)

            return response, 201

        else:
            movies = db.session.query(Movies).all()
            response = movies_schema.dump(movies)

            return response, 200

    def post(self):
        req_json = request.json
        new_movie = Movies(**req_json)
        with db.session.begin():
            db.session.add(new_movie)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        movie = db.session.query(Movies).filter(Movies.id == mid).one()
        response = movie_schema.dump(movie)

        return response, 200

    def put(self, mid: int):
        movie = db.session.query(Movies).filter(Movies.id == mid).one()
        req_json = request.json

        movie.title = req_json.get('title')
        movie.description = req_json.get('description')
        movie.trailer = req_json.get('trailer')
        movie.year = req_json.get('year')
        movie.rating = req_json.get('rating')
        movie.genre_id = req_json.get('genre_id')
        movie.director_id = req_json.get('director_id')

        db.session.add(movie)
        db.session.commit()

        return "", 204

    def patch(self, mid: int):
        movie = db.session.query(Movies).filter(Movies.id == mid).one()
        req_json = request.json

        if 'title' in req_json:
            movie.title = req_json.get('title')
        if 'description' in req_json:
            movie.description = req_json.get('description')
        if 'trailer' in req_json:
            movie.trailer = req_json.get('trailer')
        if 'year' in req_json:
            movie.year = req_json.get('year')
        if 'rating' in req_json:
            movie.rating = req_json.get('rating')
        if 'genre_id' in req_json:
            movie.genre_id = req_json.get('genre_id')
        if 'director_id' in req_json:
            movie.director_id = req_json.get('director_id')

        db.session.add(movie)
        db.session.commit()

        return "", 204

    def delete(self, mid: int):
        movie = db.session.query(Movies).filter(Movies.id == mid).one()
        db.session.delete(movie)
        db.session.commit()

        return "", 204