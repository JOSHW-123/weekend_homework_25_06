import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("No.1","No.4")
        self.song_2 = Song("No.2","No.5")
        self.song_3 = Song("No.3","No.6")

        self.jim = Guest("Jim", 200.00, 32, "Song No.1")
        self.tom = Guest("Tom", 175.00, 32, "Song No.2")

        self.guests = (self.jim, self.tom)

        self.room = Room("The First Room", 25, 10)

    def test_room_has_no_guests_at_start(self):
        self.assertEqual(0, self.room.number_of_guests())

    def test_room_has_till(self):
       self.assertEqual(0, self.room.till)

    def test_room_has_name(self):
            self.assertEqual("The First Room", self.room.name)


    def test_room_count_works(self):
        self.assertEqual(1, self.room) 

    # def test_can_check_available_rooms(self):
    #     self.assertEqual("We have rooms available", self.inventory())
        
    # def test_add_room(self):
    #     self.room.add_room(self, room_1)
    #     self.assertEqual(1, self.room.)
    #     pass

    def test_create_room_works(self):
        self.room.append(self.room)
        self.assertEqual("Room created")

    def test_can_check_in_guest(self):
        self.room.check_in_guest(self.jim)
        self.assertEqual(1, self.room.number_of_guests())
        
        

    # def test_find_guest(self):
    #     # self.room.
    #         self.assertEqual("Jim", self.number)   

    # def test_add_song(self):
    #     self.add_song(self.song_1)

    # def test_check_in_works(self):
    #     self.room_1.check_in(self.guest_1)
    #     self.assertEqual( self.inventory)


    def test_can_check_guest_out(self):
        self.room.check_in_guest(self.jim)
        self.room.check_out_guest(self.victor)
        self.assertEqual(0, self.room.number_of_guests())



        
    