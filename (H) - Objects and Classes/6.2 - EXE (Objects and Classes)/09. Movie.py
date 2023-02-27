class Movie:
    __watched_movies = 0

    def __init__(self, name: str, director: str, watched=False):
        self.name = name
        self.director = director
        self. watched = watched

    def change_name(self, new_name: str) -> None:
        self.name = new_name

    def change_director(self, new_director: str) -> None:
        self.director = new_director

    def watch(self) -> None:
        if not self.watched:   # if self.watched == False:
            self. watched = True
            Movie.__watched_movies += 1

    def __repr__(self) -> str:
        return f"Movie name: {self.name}; Movie director: {self.director}. " \
               f"Total watched movies: {Movie.__watched_movies}"


# first_movie = Movie("Inception", "Christopher Nolan")
# second_movie = Movie("The Matrix", "The Wachowskis")
# third_movie = Movie("The Predator", "Shane Black")
# first_movie.change_director("Me")
# third_movie.change_name("My Movie")
# first_movie.watch()
# third_movie.watch()
# first_movie.watch()
# print(first_movie)
# print(second_movie)
# print(third_movie)


# class Movie:
#     __watched_movies = 0
#
#     def __init__(self, name, director, watched=False):
#         self.name = name
#         self.director = director
#         self.watched = watched
#
#     def change_name(self, new_name: str):
#         self.name = new_name
#
#     def change_director(self, new_director: str):
#         self.director = new_director
#
#     def watch(self):
#         # if self.watched == False:
#         if not self.watched:
#             self.watched = True
#             Movie.__watched_movies += 1
#
#     def __repr__(self):
#         string_with_output = f"Movie name: {self.name}; Movie director: {self.director}. "
#         string_with_output += f"Total watched movies: {Movie.__watched_movies}"
#         return string_with_output
