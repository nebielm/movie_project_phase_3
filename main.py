from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv


def main():
    """creates storage instances and uses it to create the Movie App and runs it"""
    nebiel_storage = StorageJson('data.json')
    nebiel_movie_app = MovieApp(nebiel_storage)
    pamela_storage = StorageCsv("data.csv")
    pamela_movie_app = MovieApp(pamela_storage)
    pamela_movie_app.run()
    # nebiel_movie_app.run()


if __name__ == "__main__":
    main()
