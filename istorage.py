from abc import ABC, abstractmethod


class IStorage(ABC):

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def write_file(self, python_obj):
        pass

    @abstractmethod
    def list_movies(self):
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster, imdb_id, origin):
        pass

    @abstractmethod
    def delete_movie(self, title):
        pass

    @abstractmethod
    def update_movie(self, title, movie_note):
        pass
