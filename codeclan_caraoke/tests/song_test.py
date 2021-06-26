import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("The Fire by The Roots")
        self.song_2 = Song("Happy Man by Jungle")
        
        
    def test_find_song_by_name(self):
        self.assertEqual([], self.song.name)

    # def test_add_song(self):
    #     self.song.add_song(self.song_1)
    #     self.assertEqual(1, self.song.song_count())

    def add_song(self, song):
        self.playlist.append(song)
        
