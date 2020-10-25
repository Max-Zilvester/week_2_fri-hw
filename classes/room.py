class Room:
    def __init__(self, number, price, availability, playlist):
        self.number = number
        self.price = price
        self.availability = availability
        self.playlist = playlist
        self.booking = []

    # 7 pass test room has number
    def room_has_number(self):
        return self.number

    # 8  pass test room has availability
    def room_has_availability(self):
        return self.availability

    # 9  pass test room has price
    def room_has_price(self):
        return self.price

    # 13  pass test room has playlist
    def room_has_playlist(self):
        return self.playlist

    # 15  pass test add song to room
    def add_song_to_room(self, song):
        if self.availability == 1:
            self.booking.append(song)
