import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Frank Samson", 50.00, 30)

    # 1 test guest has name
    def test_guest_has_name(self):
        self.assertEqual("Frank Samson", self.guest.name)

    # 2 test guest has wallet
    def test_guest_has_wallet(self):
        self.assertEqual(50.00, self.guest.wallet)