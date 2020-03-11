from room import Room
from player import Player

# Purpose: Allows player to move between rooms


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

#

#
# Main
#

username = input('Please enter your username: ')
# Make a new player object that is currently in the 'outside' room.

user_player = Player(username, room['outside'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
user_input = ''


def get_user_input():
    return input("Next move (press 'q' to quit): ")


print("This a game where you can move to different rooms. Press 'n' to move north. Press 's' to move south. Press 'e' to move east. Press 'w' to move west. Press 'q' to quit.")
while user_input != "q":
    print(user_player.get_current_room)
    user_input = get_user_input()

print("Exited game")
