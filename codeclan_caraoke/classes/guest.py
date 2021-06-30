class Guest():

    def __init__(self, name, wallet, age, song):
        self.name = name
        self.wallet = wallet
        self.ages = age
        self.favourite_song = song
        self.shopping_list = {"beers": 2}
             

    def add_to_shopping_list(self):
            self.shopping_list["beers"] += 1
            self.shopping_list = {"beers": 2}
    add_to_shopping_list

#     def func():
#     ...     dic['a']+=1
#     ...     
#     >>> dic = {'a':1}    #dict defined before function call
#     >>> func()
#     >>> dic
#     {'a': 2}
# # status will show check in status.

    # def buy_room(self, room):
    #     if self.enough_money (room):
    #          self.wallet -= room.price

    def check_guest_has_a_name(self):
        return self.name

    def enough_money(self):
       if self.wallet >= self.price == True :
           return True
           

    def wallet_amount(self, guest):
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
