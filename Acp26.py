class Account:
    def __init__(self, owner, pin):
        self.owner = owner
        # The __ makes the PIN private and secret
        self.__pin = pin  

    # A safe way to change the secret PIN
    def change_pin(self, old_pin, new_pin):
        # 1. Check if the user knows the current PIN
        if old_pin != self.__pin:
            return "Wrong current PIN!"
        
        # 2. Check if the new PIN is exactly 4 numbers long
        if len(new_pin) != 4:
            return "PIN must be 4 numbers!"
        
        # 3. Check if the new PIN is too easy to guess
        if new_pin == "1234" or new_pin == "0000":
            return "That PIN is too weak!"
        
        # If everything is correct, save the new PIN safely
        self.__pin = new_pin
        return "PIN changed successfully!"
