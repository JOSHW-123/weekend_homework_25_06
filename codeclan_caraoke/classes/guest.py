class Guest():

    def __init__(self, name, wallet, guest_status):
        self.name = name
        self.wallet = wallet
        self.guest_status = guest_status
# status will show check in status.

    def guest_check_in_status(self, guest_status):
        if guest_status == "Checked in":
           return True
        elif guest_status == "Not checked in":
            return False

        
    def check_in(self, room, name):
        pass


    def check_out(self, room):
       pass 

  
