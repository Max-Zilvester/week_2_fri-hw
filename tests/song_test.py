import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Clint Eastwood", "Gorrilaz", "Electropop")
        self.song2 = Song("All Eyez On Me", "Tupac", "Rap")
        self.song3 = Song("Timeless", "Il Divo", "Classical")
        self.song4 = Song("Hurt", "Johnny Cash", "Country")
        self.song5 = Song("Mustang Sally", "Wilson Pinkett", "Blues")
        self.song6 = Song("Think Twice", "Celine Dion", "Soft Rock")
        self.song7 = Song("Bye Bye", "Mariah Carey", "R&B")
        self.song8 = Song("Perfect", "Ed Sheeran", "Pop")
        

    # 4 test song has title
    def test_song_has_title(self):
        self.assertEqual("Clint Eastwood", self.song.title)

    # 5 test song has artist
    def test_song_has_artist(self):
        self.assertEqual("Gorrilaz", self.song.artist)

    # 6 test song has genre
    def test_song_has_genre(self):
        self.assertEqual("Electropop", self.song.genre)
        