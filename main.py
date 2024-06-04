from movie_app import MovieApp
from storage_json import StorageJson


def main():
    nebiel_storage = StorageJson('data.json')
    nebiel_movie_app = MovieApp(nebiel_storage)
    nebiel_movie_app.run()


if __name__ == "__main__":
    main()
