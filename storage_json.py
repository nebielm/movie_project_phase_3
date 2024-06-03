from istorage import IStorage
import json


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        """Reads a Json file and returns it as a python object."""
        with open(self.file_path, "r") as json_data:
            movie_data = json.load(json_data)
        return movie_data

    def write_file(self, python_obj):
        """Converts Python object to a json string and writes a file."""
        with open(self.file_path, "w") as json_data:
            json.dump(python_obj, json_data)

    def list_movies(self):
        """Prints all movies and info's in Database."""
        movie_data = self.read_file()
        print(f"{len(movie_data)} movies in total:\n")
        for movie, info in movie_data.items():
            print(f"{movie}: {info['rating']} ({info['year']})")

    def add_movie(self, title, year, rating, poster, imdb_id, origin):
        """Adds a movie to the movie's database.
        Loads the information from the JSON file, add the movie,
        and saves it. The function doesn't need to validate the input."""
        movie_data = self.read_file()
        movie_data[title] = {"rating": rating, "year": year, "poster": poster, "imdbID": imdb_id, "origin/s": origin}
        self.write_file(movie_data)

    def delete_movie(self, title):
        """Deletes a movie from the movie's database.
        Loads the information from the JSON file, deletes the movie,
        and saves it. The function doesn't need to validate the input."""
        movie_data = self.read_file()
        movie_data.pop(title)
        self.write_file(movie_data)

    def update_movie(self, title, movie_note):
        """Updates a movie from the movie's database.
        Loads the information from the JSON file, updates the movie,
        and saves it. The function doesn't need to validate the input."""
        movie_data = self.read_file()
        movie_data[title]["note"] = movie_note
        self.write_file(movie_data)
