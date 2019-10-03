# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, items=[]):  # constructor
        self.name = name
        self.current_room = current_room
        self.items = items


    def add_items(self, item):
        self.items.append(item)

    def drop_items(self, item):
        self.items.remove(item)

    def __str__(self):
        return f"Player: {self.name} has the following items: {self.items}"

    def __repr__(self):
        pass


ramses = Player("Ramses", "Laptop")

print(ramses)
