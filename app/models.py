from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

from app.database import db


class Directors(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    movie = relationship('Movies', back_populates='director')


class Genres(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    movie = relationship('Movies', back_populates='genre')


class Movies(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    description = db.Column(db.String(250))
    trailer = db.Column(db.String(250))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))

    genre = relationship('Genres', back_populates='movie')
    director = relationship('Directors', back_populates='movie')


class DirectorSchema(Schema):
    id = fields.Integer()
    name = fields.String()


class GenreSchema(Schema):
    id = fields.Integer()
    mame = fields.String()


class MovieSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()
    trailer = fields.String()
    year = fields.Integer()
    rating = fields.Float()
    genre_id = fields.Integer()
    director_id = fields.Integer()

