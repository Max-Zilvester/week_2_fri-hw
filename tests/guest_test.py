import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.room = Room("300", 30.00, 0)
        self.guest = Guest("Frank Samson", 50.00, 30)
        self.guest2 = Guest("Johnny Bravo", 100.00, 55)
        self.guest3 = Guest("Lucy Lou", 85.00, 40)
        self.guest4 = Guest("Paul Rand", 20.00, 17)
        

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

    # test guest can check in
    # def test_guest_can_check_in(self):
    #     room = Room("300", 30.00, 0)
    #     self.guest.can_check_in(self.room)


    


    # # 8 test guest can book room
    # def test_guest_can_book_room__check_age(self):

    #     self.assertEqual(30, self.room1.availability)

    #

    # def test_add_song_to_list(self):
    #     new_song = Song("Bohemian Rhapsody", "Queen", 1975, Genre.POP)
    #     self.dukebox.add_song_to_songs(new_song)
    #     self.assertEqual("Bohemian Rhapsody", self.dukebox.songs[-1].name)  ### works fine
