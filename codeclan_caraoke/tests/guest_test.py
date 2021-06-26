import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Jim", 100, "Checked in")

    def test_find_guest(self):
        self.assertEqual("Jim", self.guest.name)



