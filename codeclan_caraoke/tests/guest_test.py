import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Jim", 100.00, "Checked in")

    def test_can_buy_room(self):
        self.guest.buy_room(self.room.inventory)
        self.assertEqual(50.00, self.guest.wallet)

    



