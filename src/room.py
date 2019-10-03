# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, description, n_to, s_to, e_to, w_to, items=[]):
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items

    def add_items(self, item):
        self.items.append(item)

    def items_removed(self, item):
        self.items.remove(item)

    def items_available(self):
        print(self.items)

    def __str__(self):
        return f"This is the {self.description} it is north to the {self.n_to} " \
               f"south to the {self.s_to} east to the {self.e_to} and west to the {self.w_to} " \
               f"in it you can find the {self.items}"

    def __repr__(self):
        pass


living_room = Room("LivingRoom", "Kitchen", "Garage", "Backyard", "Foyer", "Remote")

print(living_room)