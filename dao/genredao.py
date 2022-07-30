from dao.model.models import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all_genres(self):
        return self.session.query(Genre).all()

    def get_genre_by_id(self, id):
        return self.session.query(Genre).filter(Genre.id == id).one()
