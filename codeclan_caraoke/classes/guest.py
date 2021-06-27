class Guest():

    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.ages = age
        
        
# status will show check in status.

    def buy_room(self, room):
        if self.enough_money(room):
            self.wallet -= room.price

    def check_guest_name(self):
        return self.name

    def enough_money(self, item):
        return self.wallet >= item.price

    def return_wallet_amount(self):
        return self.wallet

    #     if status == True:
    #        return self.name + ("Checked in")
    #     elif status == False:
    #         return self.name + ("Not checked in")

        
    # def check_in(self, room, name):
    #     if room:
    #         pass


    # def check_out(self, room):
    # #    pass 

  
