class Movie:
    def __init__(self, title: str, director: str, genre: str, year: int):
        self.title = title
        self.director = director
        self.genre = genre
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year}) by {self.director}"

def movies_of_genre(movies: list, genre: str):
    return [movie for movie in movies if movie.genre == genre] # Iterates through the list of movies and returns a list of movies that match the genre
    

john_woo = Movie("A better tomorrow", "John Woo", "action", 1986)
kungfu = Movie("Chinese Odyssey", "Stephen Chow", "comedy", 1993)
jet_li = Movie("The Legend", "Corey Yuen", "comedy", 1993)

movies = [john_woo, kungfu, jet_li, Movie("Hero", "Yimou Zhang", "action", 2002)]

print("Movies in the action genre:")
for movie in movies_of_genre(movies, "action"):
    print(f"{movie.director}: {movie.title}")