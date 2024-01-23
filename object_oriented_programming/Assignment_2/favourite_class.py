class Song:

    def __init__(self, title: str, artist: str, year: int, genre: str):
        self.title = title
        self.artist = artist
        self.year = year
        self.genre = genre


first_song = Song("The Sound of Silence", "Simon & Garfunkel", 1964, "Folk Rock")
second_song = Song("The Boxer", "Simon & Garfunkel", 1969, "Folk Rock")

print(f"{first_song.title}: {first_song.artist} from {first_song.year} in the genre {first_song.genre}")
print(f"The genre of second song is {second_song.genre} and the song name is {second_song.title}")

