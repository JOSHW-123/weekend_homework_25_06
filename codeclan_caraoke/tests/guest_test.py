import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Jim", 200.00, 32)

    def test_can_buy_room(self):
        self.assertEqual(50.00, self.guest.buy_room)

    def test_guest_has_name(self):
        self.assertEqual("Jim", self.guest.name)

    def test_enough_money_true(self):
        self.assertEqual("You have enough money", self.guest.enough_money)

    def test_guest_has_wallet(self):
        self.assertEqual(200.00, self.guest.wallet)
    
    def test_add_favourite_song(self):
        self.favourite_song = {}
        self.add_favourite_song(self,)
        self.assertEqual([{"The Fire" : "The Roots"}])

       