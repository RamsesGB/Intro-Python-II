from room import Room

from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",  ),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Adding items to each room
room['treasure'].add_items("Coins")
room['narrow'].add_items("Rope")
room['foyer'].add_items("Sandwich")
room['overlook'].add_items("Sword")



# Main
print("Welcome to PythonLand")
print("Please choose an option to control your character")
# Make a new player object that is currently in the 'outside' room.
# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

ramses = Player('Ramses', room['outside'])

#ramses.add_items("Test")

#print(ramses.items)

user = ""

valid = ["n", "s", "e", "w",]

inventory = "i"



while not user == "q":
    user = input("Where would you like to go [N] North | [S] South | [E] East | [W] West | [Q] Quit\n")
    #Adventure begins
    if user in valid:
        ramses.move(user)
        #print(f"{ramses.name} you find yourself at the {ramses.current_room.name}, {ramses.current_room.description}")

    elif user in inventory:
        print(f"Your Inventory {ramses.item}")

    elif user not in valid:
        ramses.handleVerb(user)

    else:
        print(f"Invalid selection please try again")