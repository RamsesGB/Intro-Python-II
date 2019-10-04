from room import Room

from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

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

# Add item to a room example -> room['treasure'].add_items()

# Main
print("Welcome to PythonLand")
print("Please choose an option to control your character")

user = int(input("[1]New Adventure    [9]At anytime to quit\n"))
# Make a new player object that is currently in the 'outside' room.
ramses = Player('Ramses', room['outside'])
# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
def reset_loop(user, num):
    temp = num
    temp2 = user
    user = temp
    return user

while not user == 9:
    #Adventure begins
    if user == 1: #OUTSIDE
        ramses.change_room(room['foyer'].s_to)
        print(f"{ramses.name} you find yourself at the {ramses.current_room.name}, {ramses.current_room.description}")
        user = int(input("what would you like to do next? [2] Travel North |  [9] Quit\n"))

    elif user == 2: #FOYER
        ramses.change_room(room['outside'].n_to)
        print(f"{ramses.name} you find yourself at the {ramses.current_room.name}, {ramses.current_room.description}")
        print(f"You can travel south to the {ramses.current_room.s_to.name}, north to the {ramses.current_room.n_to.name}, or east to the {ramses.current_room.e_to.name}")
        user = int(input(f"[1] Travel South | [3] Travel North | [4] Travel East | [9] Quit \n"))
        if user == 3: #OVERLOOK
            ramses.change_room(room['foyer'].n_to)
            print(f"{ramses.name} you find yourself at the {ramses.current_room.name}, {ramses.current_room.description}")
            user = int(input(f"The only exit is to the North [2] Travel North | [9] Quit\n"))
        elif user == 4: #NARROW
            ramses.change_room(room['foyer'].e_to)
            print(f"{ramses.name} you find yourself at the {ramses.current_room.name}, {ramses.current_room.description}")
            user = int(input("Pursue the smell of gold? or cowardly return West | [5] Travel North | [3] Travel West [9] Quit\n"))
            if user == 5:#TREASURE
                ramses.change_room(room['narrow'].n_to)
                print(f"{ramses.name} you find yourself at the {ramses.current_room.name}, {ramses.current_room.description}")
                user = int(input(f"The only exit is to the South [4] Travel South | [9] Quit\n"))
    else:
        print(f"Invalid selection please try again")
        user = int(input("You have completed the adventure [9] Go Home"))