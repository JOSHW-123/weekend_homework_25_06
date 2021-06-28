class Guest():

    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.ages = age
        self.favourite_song = {}

        
        
# status will show check in status.

    def buy_room(self, room):
            self.wallet -= room.price

    def check_guest_name(self):
        return self.name

    def enough_money(self, room):
        if self.wallet > room.price :
            return "You have enough money"
        else:
            return "Sorry you cant afford this"

    def wallet_amount(self):
        return self.wallet

    def add_favourite_song(self, ):
        self.favourite_song["The Fire"] = "The Roots"
        print(self.favourite_song)

    #     if status == True:
    #        return self.name + ("Checked in")
    #     elif status == False:
    #         return self.name + ("Not checked in")

        
    # def check_in(self, room, name):
    #     if room:
    #         pass


    # def check_out(self, room):
    # #    pass 

  
