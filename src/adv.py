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

#
# Main
#
# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
while True:
    print(player.current_room.name)
    print(player.current_room.description)
    print('\n')
    user_input = input('Enter Directions: ').lower()[0]
    print('\n')
    print(user_input)

    if player.current_room.name == 'Outside Cave Entrance' and user_input == 'n':
        player.current_room = room['foyer']
        print(player.current_room.name)
        print('\n')
    elif player.current_room.name == 'Outside Cave Entrance' and user_input != 'n':
        print('You can only go north from this room!')
        print('\n')
    if player.current_room.name == 'Foyer' and user_input == 's':
        player.current_room = room['outside']
        print(player.current_room.name)
        print('\n')
    elif player.current_room.name == 'Foyer' and user_input == 'n':
        player.current_room = room['overlook']
        print(player.current_room.name)
        print('\n')
    elif player.current_room.name == 'Foyer' and user_input == 'e':
        player.current_room = room['narrow']
        print(player.current_room.name)
        print('\n')
    elif player.current_room.name == 'Foyer' and user_input != 's' or user_input != 'n' or user_input != 'e':
        print('You can only go north, south, or east from this room!')
        print('\n')
    if player.current_room.name == 'Grand Overlook' and user_input == 's':
        player.current_room = room['foyer']
        print(player.current_room.name)
        print('\n')
    elif player.current_room.name == 'Grand Overlook' and user_input != 's':
        print('You can only go south from this room!')
        print('\n')
    if player.current_room.name == 'Narrow Passage' and user_input == 'w':
        player.current_room = room['foyer']
        print(player.current_room.name)
        print('\n')
    elif player.current_room.name == 'Narrow Passage' and user_input == 'n':
        player.current_room = room['treasure']
        print(player.current_room.name)
        print('\n')
    elif player.current_room.name == 'Narrow Passage' and user_input != 'w' or user_input != 'n':
        print('You can only go west or north from this room!')
        print('\n')
    if player.current_room.name == 'Treasure Chamber' and user_input == 's':
        player.current_room = room['narrow']
        print(player.current_room.name)
        print('\n')
    elif player.current_room.name == 'Treasure Chamber' and user_input != 's':
        print('You can only go south from this room!')
        print('\n')
    if user_input == 'q':
        print('Goodbye')
        break

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
