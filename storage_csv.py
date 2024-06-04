from istorage import IStorage
import ast


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        """Reads a Json file and returns it as a python object."""
        with open(self.file_path, "r") as csv_data:
            movie_data = csv_data.read()
        movies_list = [line.strip() for line in movie_data.split("\n") if line.strip()]
        info_titles = movies_list[0].split(";")
        dict_movie_data = {}
        for movie in movies_list[1:]:
            movie_infos = movie.split(";")
            dict_movie_data[movie_infos[0]] = {}
            for i, info in enumerate(movie_infos[1:]):
                try:
                    if info_titles[i + 1] == "rating":
                        dict_movie_data[movie_infos[0]][info_titles[i + 1]] = float(info)
                    elif info_titles[i + 1] == "year":
                        dict_movie_data[movie_infos[0]][info_titles[i + 1]] = int(info)
                    elif info_titles[i + 1] == "origin/s":
                        dict_movie_data[movie_infos[0]][info_titles[i + 1]] = ast.literal_eval(info)
                    else:
                        dict_movie_data[movie_infos[0]][info_titles[i + 1]] = str(info)
                except Exception as e:
                    print(e)
        return dict_movie_data

    def write_file(self, python_obj):
        """Converts Python object to a json string and writes a file."""
        csv_obj = "title;rating;year;poster;imdbID;origin/s;note\n"
        for title, info in python_obj.items():
            csv_obj += (f"{title};{info["rating"]};{info["year"]};"
                        f"{info["poster"]};{info["imdbID"]};{info["origin/s"]}")
            if len(info) == 6:
                csv_obj += f";{info["note"]}\n"
            else:
                csv_obj += "\n"
        with open(self.file_path, "w") as csv_file:
            csv_file.write(csv_obj)

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
