import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("The Fire : The Roots", "Playlist_1")
        
        
    def test_find_song_by_name(self):
        self.assertEqual("The Fire : The Roots", self.song.name)
