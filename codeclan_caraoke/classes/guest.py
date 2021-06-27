class Guest():

    def __init__(self, name, wallet, status):
        self.name = name
        self.wallet = wallet
        self.bill = 0
        self.status = status
# status will show check in status.

    def buy_room(self, room):
        if self.enough_money(room):
            self.wallet -= room.price


    def enough_money(self, item):
        return self.wallet >= item.price



    #     if status == True:
    #        return self.name + ("Checked in")
    #     elif status == False:
    #         return self.name + ("Not checked in")

        
    # def check_in(self, room, name):
    #     if room:
    #         pass


    # def check_out(self, room):
    # #    pass 

  
