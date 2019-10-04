# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):  # constructor
        self.name = name
        self.current_room = current_room
        self.items = []

    def add_items(self, item):
        self.items.append(item)

    def drop_items(self, item):
        self.items.remove(item)

    def change_room(self, new_room):
        self.current_room = new_room

    def __str__(self):
        return f"Player -> {self.name} is in the {self.current_room} and has the following items: {self.items}"

    def __repr__(self):
        pass
