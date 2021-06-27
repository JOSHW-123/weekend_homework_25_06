class Room:

    def __init__(self, price, number, inventory, playlist):
        self.number = number
        self.price = price
        self.playlist = playlist
        self.inventory = inventory
        self.arrivals = []


    def room_count(self):
        return len(self.room.inventory)

    def check_available_rooms(self):
        if self.inventory >= self.arrivals:
            return "We have rooms available"
        else:
            return "We have no rooms available"

    # def add_room(self, room):
    #     self.inventory.append(room)

    def add_guest(self, arrivals):
        self.arrivals.append(arrivals)

    def add_room(self, room):
        if 0 in self.inventory:
            self.inventory[room] += 1
        else:
            self.inventory[room] = 1

    def check_in(self, guest):
        if self.inventory > 0 :
            self.guest.bill += self.price

    def add_song(self, song):
        self.playlist.append(song)

    def find_guest(self, name):
        if name in self.arrivals == name :
            return name