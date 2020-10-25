import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.song = Song("Clint Eastwood", "Gorrilaz", "Electropop")
        self.song2 = Song("All Eyez On Me", "Tupac", "Rap")
        self.song3 = Song("Timeless", "Il Divo", "Classical")
        self.song4 = Song("Hurt", "Johnny Cash", "Country")
        self.song5 = Song("Mustang Sally", "Wilson Pinkett", "Blues")
        self.song6 = Song("Think Twice", "Celine Dion", "Soft Rock")
        self.song7 = Song("Bye Bye", "Mariah Carey", "R&B")
        self.song8 = Song("Perfect", "Ed Sheeran", "Pop")
        
        self.room = Room("300", 30.00, 0, [self.song, self.song2])
        self.guest = Guest("Frank Samson", 50.00, 30, self.song3)
        self.guest2 = Guest("Johnny Bravo", 100.00, 55, self.song4)
        self.guest3 = Guest("Lucy Lou", 85.00, 40, self.song5)
        self.guest4 = Guest("Paul Rand", 20.00, 17, self.song6)
        

    # 1 test guest has name
    def test_guest_has_name(self):
        self.assertEqual("Frank Samson", self.guest.name)

    # 2 test guest has wallet
    def test_guest_has_wallet(self):
        self.assertEqual(50.00, self.guest.wallet)

    # 3 test guest age
    def test_guest_age(self):
        self.assertEqual(30, self.guest.age)


    # 10 test guest can book a room.
    def test_guest_can_book_a_room(self):
        self.guest.book_room(self.room)
        self.assertEqual(20, self.guest.wallet)

    # 11 guest checks in
    def test_guest_check_in(self):
        #self.room_has_availability(self.room)
        self.guest.check_in(self.room)
        self.assertEqual(1, self.room.availability)

    # 12 guest checks out
    def test_guest_check_out(self):
        #self.room_has_availability(self.room)
        self.guest.check_out(self.room)
        self.assertEqual(0, self.room.availability)

    # 14 guest has favourite song
    def test_guest_has_favourite_song(self):
        self.assertEqual(self.song3, self.guest.playlist)


    # def test_guest_has_favourite_song
    # 

    # test guest can check in
    # def test_guest_can_check_in(self):
    #     room = Room("300", 30.00, 0)
    #     self.guest.can_check_in(self.room)


    


    # # 8 test guest can book room
    # def test_guest_can_book_room__check_age(self):

    #     self.assertEqual(30, self.room1.availability)

