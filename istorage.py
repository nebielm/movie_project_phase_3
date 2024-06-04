from abc import ABC, abstractmethod


class IStorage(ABC):
    """Abstract base class for storage handling"""

    @abstractmethod
    def read_file(self):
        """defines abstract method to read file"""
        pass

    @abstractmethod
    def write_file(self, python_obj):
        """defines abstract method to write file"""
        pass

    @abstractmethod
    def list_movies(self):
        """defines abstract method to list movies"""
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster, imdb_id, origin):
        """defines abstract method to add movies"""
        pass

    @abstractmethod
    def delete_movie(self, title):
        """defines abstract method to delete movie"""
        pass

    @abstractmethod
    def update_movie(self, title, movie_note):
        """defines abstract method to update movie"""
        pass
