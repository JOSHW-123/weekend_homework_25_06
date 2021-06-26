import unittest
from classes.room import Room
from classes.guest import Guest


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room()