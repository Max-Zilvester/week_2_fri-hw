class Guest:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age

    # 1 pass test guest has name
    def guest_has_name(self):
        return self.name

    # 2 pass test guest has wallet
    def guest_has_wallet(self):
        return self.wallet

    # 3 pass test check guest age
    def guest_age(self):
        return self.age

    # 10 pass test guest can book room
    def book_room(self, room):
        self.wallet -= room.price

     # check_in
    def check_in(self, room):
        if self.wallet > room.price and room.availability == 0:
            room.availability += 1
    #     if self.age >= 17:
    #         self.room.availability == 1

    # def add_stock(self, quantity=1):
    #     self.stock += quantity

    # def remove_stock(self, quantity=1):
    #     if self.has_stock(self, quantity):
    #         self.stock -= quantity