# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):  # constructor
        self.name = name
        self.current_room = current_room
        self.item = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def add_items(self, item):
        self.items.append(item)

    def drop_items(self, item):
        self.items.remove(item)

    def move(self,direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(f"\nLOCATION: {self.current_room.name}\n"
                  f"DESCRIPTION: {self.current_room.description}\n"
                  f"NEAR BY ITEMS: {self.current_room.item}")
        else:
            print(f"\nNowhere to go!\n")

    def handleVerb(self,verb):
        verb = verb.split(" ")
        if verb[0] == "take":
            if verb[1] in self.current_room.item:
                self.current_room.item.remove(verb[1])
                self.item.append(verb[1])
                return print(f"You have picked up {verb[1]}")
            else:
                print("Invalid Item take")
        elif verb[0] == "drop":
            if verb[1] not in self.current_room.item:
                self.item.remove(verb[1])
                self.current_room.item.append(verb[1])
                return print(f"You have dropped {verb[1]}")
            else:
                print("Invalid Item drop")

    def __str__(self):
        return f"Player -> {self.name} is in the {self.current_room} and has the following items: {self.items}"

    def __repr__(self):
        pass