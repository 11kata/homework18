from flask import request
from flask_restx import Resource, Namespace

from dao.model.schema import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema(many=True)
movie_schema_one = MovieSchema()


@movie_ns.route('/')
# @movie_ns.param('director_id')
# @movie_ns.param('genre_id')
# @movie_ns.param('year')
class MoviesView(Resource):
    def get(self):
        """ Отвечает за получение всех фильмов"""
        if director_id := request.args.get('director_id'):
            return movie_schema.dump(movie_service.get_movie_id(director_id=director_id))

        elif genre_id := request.args.get('genre_id'):
            return movie_schema.dump(movie_service.get_movie_id(genre_id=genre_id))

        elif year := request.args.get('year'):
            return movie_schema.dump(movie_service.get_movie_id(year=year))

        else:
            return movie_schema.dump(movie_service.get_movies()), 200


def post(self):
    """ Добавление нового фильма"""
    movie_service.add_movie(request.json)
    return "", 201


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id):
        """ Отвечает за получение фильмов по movie_id"""

        return movie_schema_one.dump(movie_service.get_movie_by(movie_id)), 200

    def put(self, movie_id):
        """ Добавление нового фильма по movie_id"""
        movie_service.update_movie(request.json)  # Метод, который изменяет фильм по id
        return "Фильм успешно изменен ", 201

    def delete(self, movie_id):
        """ Удалит фильм по movie_id"""
        movie_service.delete_movie(request.json) # Метод, который удаляет фильм по id
        return "Фильм успешно удален", 201
