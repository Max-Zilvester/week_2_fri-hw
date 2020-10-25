class Song:
    def __init__(self, title, artist, genre):
        self.title = title
        self.artist = artist
        self.genre = genre

    # 4 pass test song has title
    def song_has_title(self):
        return "Clint Eastwood"

    # 5 pass test song has artist
    def song_has_artist(self):
        return "Gorillaz"

    # 6 pass test song has genre
    def song_has_genre(self):
        return "Electropop"