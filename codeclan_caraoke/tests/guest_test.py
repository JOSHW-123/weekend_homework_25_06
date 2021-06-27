import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Jim", 100.00, 32)

    def test_can_buy_room(self):
        self.assertEqual(50.00, self.guest.buy_room)

    def test_guest_has_name(self):
        self.assertEqual("Jim", self.guest.name)

    def test_enough_money_true(self):
        self.assertEqual(True, self.guest.enough_money)

    def test_guest_has_wallet(self):
        self.assertEqual(100.00, self.guest.wallet)
