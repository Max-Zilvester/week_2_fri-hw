import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Clint Eastwood", "Gorrilaz", "Electropop")

    # 3 test song has title
    def test_song_has_title(self):
        self.assertEqual("Clint Eastwood", self.song.title)

    # 4 test song has artist
    def test_song_has_artist(self):
        self.assertEqual("Gorrilaz", self.song.artist)
        