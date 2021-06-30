import unittest

from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.song_1 = Song("No.1","No.4")
        self.song_2 = Song("No.2","No.5")
        self.song_3 = Song("No.3","No.6")

        self.songs = [self.song_1, self.song_2, self.song_3]

        song = Song("No.3","No.6")
        self.guest = Guest("Jim", 200.00, song)

    def test_guest_has_name(self):
        self.assertEqual("Jim", self.guest.name)

    def test_guest_has_cash(self):
        self.assertEqual(200.00, self.guest.wallet)
    
    # def test_can_buy_room(self):
    #     self.guest_1.buy_room(self.guest_1)
    #     self.assertEqual(True, self.guest_1.wallet)
    # def test_item_added_to_shopping_list(self):

    def test_if_guest_has_enough_money_true(self):
        self.assertEqual(200.00, self.guest_1.wallet)

    def test_guest_has_wallet(self):
        self.assertEqual(200.00, self.guest_1.wallet)
    
    # def test_add_favourite_song(self):
    #     self.add_favourite_song 
    #     self.assertFalse
    #         pass
