import unittest
from classes.room import Room
from classes.guest import Guest


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Occupied", 1, 50, "Jim playlist")
        self.room_2 = Room("Occupied", 2, 100, "Jon playlist")

    def test_room_count(self):
        self.assertEqual(self.room.inventory) 

    # def test_add_room(self):
    #     self.room.add_room(self, room_1)
    #     self.assertEqual(1, self.room.)
    #     pass

    def test_add_room(self):
        self.room_1.add_room(self.room_1)
        self.assertEqual(1, self.room_count)

    def test_find_guest(self):
            self.assertEqual("Jim", self.room.name)   

    
        