class Song:
    def __init__(self, title, artist, genre):
        self.title = title
        self.artist = artist
        self.genre = genre

    # 4 pass test song has title
    def song_has_title(self):
        return self.title

    # 5 pass test song has artist
    def song_has_artist(self):
        return self.artist

    # 6 pass test song has genre
    def song_has_genre(self):
        return self.genre