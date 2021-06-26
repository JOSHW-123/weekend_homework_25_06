import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Jim", 100, "Checked in")

    def test_check_in_status(self):
        self.assertEqual("Checked in", self.guest.guest_status)



