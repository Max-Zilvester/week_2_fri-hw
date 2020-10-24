import unittest
from classes.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(300, True)

    # 6 test room has number
    def test_room_has_number(self):
        self.assertEqual(300, self.room.number)

    # 7 test room has availability
    def test_room_has_availability(self):
        self.assertEqual(True, self.room.availability)