import unittest
from classes.room import Room
from classes.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Frank Samson", 50.00, 30)
        self.room = Room("300", 30.00, 0)
        self.room2 = Room("301", 25.00, 1)
        self.room3 = Room("302",20.00, 1)
        self.room4 = Room("303", 30.00, 0)
        
        

    # 7 test room has number
    def test_room_has_number(self):
        self.assertEqual("300", self.room.number)

    # 8 test room has availability
    def test_room_has_availability(self):
        self.assertEqual(0, self.room.availability)
    
    # 9 test room has price
    def test_room_has_price(self):
        self.assertEqual(30, self.room.price)

    # # 9 test guest can check in
    # def test_guest_can_book_room__check_age(self):
    #     self.room.guest_age(self.age, self.guest1)
    #     self.assertEqual(30, self.room1.availability)
