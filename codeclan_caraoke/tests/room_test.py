import unittest
from classes.room import Room
from classes.guest import Guest


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room(1, 50, ["Happy Man", "The Fire"], False, None)

    # def test_room_count(self):
    #     self.assertEqual(self.inventory) 

    # def test_can_check_available_rooms(self):
    #     self.assertEqual("We have rooms available", self.inventory())
        
    # def test_add_room(self):
    #     self.room.add_room(self, room_1)
    #     self.assertEqual(1, self.room.)
    #     pass

    # def test_add_room(self):
    #     self.room_1.add_room(self.room_1)
    #     self.assertEqual(1, self.room_count)

    # def test_find_guest(self):
    #     # self.room.
    #         self.assertEqual("Jim", self.number)   

    def test_add_song(self):
        self.room.add_song(self.song_1)
        
    
        