class Room:

    def __init__(self, name, price, capacity) :
        self.name = name
        self.price = price
        self.capacity = capacity
        self.songs = []
        self.till = 0
        self.guests = []

    def number_of_guests(self):
            return len(self.guests)

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
        if self.guests <= self.capacity:
            self.capacity[room] += 1
        else:
            self.capacity[room] = 1
            
       

    # def check_in(self, guest):
    #     if guest in self.guest.wallet >= self.price :
    #         self.guest.bill += self.price
    #     return "You can check in"

    # def check_in(self, guest_name):
    #     self.occupied = True
    #     self.guest_user = guest_name
    #     return "Guest checked in"

    # def check_in(self, guest):
    #     if guest.wallet >= self.price :
    #         guest.wallet -= self.price
    #         self.till += self.price
    #         self.occupants.append(guest)
           
           
    def check_in_guest(self, guest):
        if self.free_spaces() > 0 and guest.can_afford(self.fee):
           guest.pay(self.fee)
           self.till += self.fee
           self.guests.append(guest)
        


    def check_out_guest(self, guest):
        self.guests.remove(guest)

    # def check_out(self, guest):
    #     if guest == guest in self.occupants.pop(guest):
    #         return "You aare checked out"

    
    def add_song(self, song_name):
        self.playlist.append(song_name)

    def find_guest(self, guest):
        if guest in self.occupants == guest :
            return guest + self.number