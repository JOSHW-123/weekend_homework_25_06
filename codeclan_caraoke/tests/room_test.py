import unittest
from classes.room import Room
from classes.guest import Guest


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Room No.1", 50.00, 0)
        self.room_2 = Room("Room No.2", 75.00, 0)
        self.room_3 = Room("Room No.3", 95.00, 0)

        self.guest_1 = Guest("Jim", 200.00, 32)
        self.guest_2 = Guest("Tom", 175.00, 32)
        self.inventory = []

    def test_room_has_till(self):
       self.assertEqual(0, self.room_1.till)


    def test_room_count_works(self):
        self.assertEqual([], self.inventory) 

    # def test_can_check_available_rooms(self):
    #     self.assertEqual("We have rooms available", self.inventory())
        
    # def test_add_room(self):
    #     self.room.add_room(self, room_1)
    #     self.assertEqual(1, self.room.)
    #     pass

    def test_create_room_works(self):
        self.inventory.append(self.inventory, )
        self.assertEqual("Room created")
        
        

    # def test_find_guest(self):
    #     # self.room.
    #         self.assertEqual("Jim", self.number)   

    # def test_add_song(self):
    #     self.add_song(self.song_1)

    def test_check_in_works(self):
        self.room_1.check_in(self.guest_1)
        self.assertEqual("You are checked in", self.inventory)


    def test_check_out_works(self):
        self.room_1.check_out(self.guest_1)

        
    