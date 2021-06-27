import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("The Fire", "The Roots")
        self.song_2 = Song("Happy Man", "Jungle")
        
    def test_check_if_song_in_library(self):
        self.assertEqual("We have this song", self.song_1)

    def test_add_song(self):
        self.library.add_song(self.song_1)
        self.library.add_song(self.song_2)
        

    
        
