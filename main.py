from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv


def main():
    #nebiel_storage = StorageJson('data.json')
    #nebiel_movie_app = MovieApp(nebiel_storage)
    #nebiel_movie_app.run()
    pamela_storage = StorageCsv("data.csv")
    pamela_movie_app = MovieApp(pamela_storage)
    pamela_movie_app.run()


if __name__ == "__main__":
    main()
