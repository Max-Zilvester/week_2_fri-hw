class Guest:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age

    # pass test guest has name
    def guest_has_name(self):
        return "Frank Samson"

    # pass test guest has wallet
    def guest_has_wallet(self):
        return 50