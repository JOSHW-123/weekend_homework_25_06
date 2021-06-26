class Room:

    def __init__(self, price, room, inventory):
        self.room = room
        self.price = price
        self.inventory = {}


    def room_count(self):
        return len(self.inventory)

    def add_room(self, room):
        self.inventory.append(room)

    # def add_room(self, room):
    #     if room in self.inventory:
    #         self.inventory[room] += 1
    #     else:
    #         self.inventory[room] = 1