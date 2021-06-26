import unittest
from classes.room import Room
from classes.guest import Guest


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Occupied", 2, 100)

    def test_room_count_works(self):
        self.assertEqual([], self.room.inventory) 