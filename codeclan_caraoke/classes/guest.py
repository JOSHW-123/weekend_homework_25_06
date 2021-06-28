class Guest():

    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.ages = age
             
# status will show check in status.

    # def buy_room(self, room):
    #     if self.enough_money (room):
    #          self.wallet -= room.price

    def check_guest_has_a_name(self):
        return self.name

    def enough_money(self):
        return self.wallet >= self.price 
           

    def wallet_amount(self):
        return self.wallet

    # def add_favourite_song(self):
    #     self.favourite_song[
    #         pass
       

    #     if status == True:
    #        return self.name + ("Checked in")
    #     elif status == False:
    #         return self.name + ("Not checked in")

        
    # def check_in(self, room, name):
    #     if room:
    #         pass


    # def check_out(self, room):
    # #    pass 
