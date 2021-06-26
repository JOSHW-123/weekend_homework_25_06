class Room:

    def __init__(self, price, name, inventory, playlist):
        self.name = name
        self.price = price
        self.playlist = playlist
        self.inventory = inventory
        self.arrivals = []


    def room_count(self):
        return len(self.room.inventory)

    # def add_room(self, room):
    #     self.inventory.append(room)

    def add_guest(self, arrivals):
        self.arrivals.append(arrivals)

    def add_room(self, room):
        if room in self.inventory:
            self.inventory[room] += 1
        else:
            self.inventory[room] = 1

    def check_in(self, guest):
        if self.inventory > 0 :
            self.guest.bill += self.price