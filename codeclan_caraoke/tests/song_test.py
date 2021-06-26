import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("The Fire", "The Roots", "library_1")
        self.song_2 = Song("Happy Man", "Jungle", "library_1")
        
        
        
    # def test_find_song_by_name(self):
    #     self.assertEqual("The Fire", self.library)

    def test_add_song(self):
        self.library.add_song(self.song_1)
        self.library.add_song(self.song_2)
        

    
        
