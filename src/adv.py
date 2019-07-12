from room import Room
from player import Player
from item import Item


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

treasure_map = Item('map', 'Leads to the treasure')
key = Item('key', 'Opens the treasure chest')
chest = Item('chest', 'Holds the treasure')


room['outside'].items.append(treasure_map)
room['overlook'].items.append(key)
room['treasure'].items.append(chest)

#
# Main
#
# Make a new player object that is currently in the 'outside' room.
player = Player("Guillaume", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#

valid_directions = ['n', 's', 'w', 'e']
valid_tasks = ['get', 'drop', 'open']

while True:
    # Wait for user input
    cmd = input("-> ").lower().split()
    cmd1 = cmd[0]
    # print(len(cmd))
    if len(cmd) > 1:
        cmd2 = cmd[1]
    # Parse user inputs (n, s, e, w, q)
    if cmd1 in valid_directions:
        # If input is valid, move the player and loop
        player.travel(cmd1)
    elif cmd1 == "i":
        print(player.print_inventory())
    elif cmd1 == "q":
        print("Goodbye!")
        exit()
    elif cmd1 in valid_tasks:
        if cmd1 == 'get':
            for i in player.current_room.items:
                # Check if item exist in the room
                if i.name == cmd2:
                    player.get(i)
                    print(player.current_room.remove_item(i))
                else:
                    print(f"Sorry there is no {cmd2} in the room")
        if cmd1 == 'drop':
            for i in player.items:
                # Check if item exist in the room
                if i.name == cmd2:
                    player.drop(i)
                    print(player.current_room.add_item(i))
                else:
                    print(f"Sorry there is no {cmd2} in the room")
    else:
        print("I did not recognize that command")
