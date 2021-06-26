import unittest
from classes.room import Room
from classes.guest import Guest


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Occupied", 1, 50)
        self.room_2 = Room("Occupied", 2, 100)

    # def test_room_count(self):
    #     self.assertEqual(self.room.inventory) 

    # def test_add_room(self):
    #     self.room.add_room(self, room_1)
    #     self.assertEqual(1, self.room.)
    #     pass

    def test_add_room(self):
        self.room.add_room(self.room_1)
        self.assertEqual(1, self.room.room_count())
        