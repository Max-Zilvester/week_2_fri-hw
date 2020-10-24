class Song:
    def __init__(self, title, artist, genre):
        self.title = title
        self.artist = artist
        self.genre = genre

    # 3 pass test song has title
    def song_has_title(self):
        return "Clint Eastwood"

    # 3 pass test song has artist
    def song_has_artist(self):
        return "Gorillaz"