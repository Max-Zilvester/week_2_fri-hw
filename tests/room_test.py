import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):

        self.song = Song("Clint Eastwood", "Gorrilaz", "Electropop")
        self.song2 = Song("All Eyez On Me", "Tupac", "Rap")
        self.song3 = Song("Timeless", "Il Divo", "Classical")
        self.song4 = Song("Hurt", "Johnny Cash", "Country")
        self.song5 = Song("Mustang Sally", "Wilson Pinkett", "Blues")
        self.song6 = Song("Think Twice", "Celine Dion", "Soft Rock")
        self.song7 = Song("Bye Bye", "Mariah Carey", "R&B")
        self.song8 = Song("Perfect", "Ed Sheeran", "Pop")
        self.guest = Guest("Frank Samson", 50.00, 30, self.song)
        self.room = Room("300", 30.00, 0, [self.song, self.song2])
        self.room2 = Room("301", 25.00, 1, [self.song3, self.song4])
        self.room3 = Room("302", 20.00, 1, [self.song5, self.song6])
        self.room4 = Room("303", 30.00, 0, [self.song7, self.song8])
        
        

    # 7 test room has number
    def test_room_has_number(self):
        self.assertEqual("300", self.room.number)

    # 8 test room has availability
    def test_room_has_availability(self):
        self.assertEqual(0, self.room.availability)
    
    # 9 test room has price
    def test_room_has_price(self):
        self.assertEqual(30, self.room.price)

    # 13 test room has playlist
    def test_room_has_playlist(self):
        self.assertEqual(2, len(self.room.playlist))

    # 15 test add songs to room
    def test_add_song_to_room(self):
        self.room.add_song_to_room(self)
        self.assertEqual([], self.room2.booking)

