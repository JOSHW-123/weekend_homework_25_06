class Room:

    def __init__(self, number, price, till) :
        self.number = number
        self.price = price
        self.playlist = []
        self.occupants = []
        self.till = till
        self.inventory = []


    def room_count(self):
        return len(self.occupants)

    # def check_available_rooms(self):
    #     if self.inventory > self.arrivals:
    #         return "We have rooms available"
    #     else:
    #         return "We have no rooms available"


    # def add_room(self, room):
    #     self.inventory.append(room)

    # def add_guest(self, arrivals):
    #     self.arrivals.append(arrivals)

    def create_room(self, room):
        if self.occupants <= self.inventory:
            self.occupants[room] += 1
        else:
            self.occupants[room] = 1
            return "Room created"
       

    # def check_in(self, guest):
    #     if guest in self.guest.wallet >= self.price :
    #         self.guest.bill += self.price
    #     return "You can check in"

    # def check_in(self, guest_name):
    #     self.occupied = True
    #     self.guest_user = guest_name
    #     return "Guest checked in"

    def check_in(self, guest):
        if guest.wallet >= self.price :
            guest.wallet -= self.price
            self.till += self.price
            self.occupants.append(guest)
        return "You are checked in"



    def check_out(self, guest):
        self.guests.remove(guest)

    
    def add_song(self, song_name):
        self.playlist.append(song_name)

    def find_guest(self, guest):
        if guest in self.arrivals == guest :
            return guest + self.number