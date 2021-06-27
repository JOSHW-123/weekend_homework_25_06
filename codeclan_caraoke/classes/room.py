class Room:

    def __init__(self, number, price, playlist, occupied, guest_user) :
        self.number = number
        self.price = 50
        self.playlist = ["Happy Man", "The Fire"]
        self.occupied = False
        self.guest_user = None 
        self.arrivals = []


    def room_count(self):
        return len(self.arrivals)

    # def check_available_rooms(self):
    #     if self.inventory > self.arrivals:
    #         return "We have rooms available"
    #     else:
    #         return "We have no rooms available"


    # def add_room(self, room):
    #     self.inventory.append(room)

    def add_guest(self, arrivals):
        self.arrivals.append(arrivals)

    # def add_room(self, room):
    #     if self.room_count in self.inventory:
    #         self.inventory[room] += 1
    #     else:
    #         self.inventory[room] = 1
       

    # def check_in(self, guest):
    #     if guest in self.guest.wallet >= self.price :
    #         self.guest.bill += self.price
    #     return "You can check in"

    def check_in(self, guest_name):
        self.occupied = True
        self.guest_user = guest_name
        return "Guest checked in"

    def check_out(self, guest_name):
        self.occupied = False
        self.guest_user = None
        return "Guest checked out"

    
    def add_song(self, song_name):
        self.playlist.append(song_name)

    def find_guest(self, guest):
        if guest in self.arrivals == guest :
            return guest + self.number