from room import Room
from player import Player
from item import Item

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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['outside'].items = [Item('vase', 'a dang vase'), Item('gun', 'a pistol with no bullets'), Item('egg', 'Did it come first?'), Item('rose', 'a dying but beautiful rose')]
room['foyer'].items = [Item('umbrella', 'its broken!'), Item('basket', 'who would want this?')]
room['treasure'].items = [Item('empty chest', 'where\'s the cash, man?'), Item('ruby', 'Rubies are a girl\'s bestfriend...wait')]
room['narrow'].items = [Item('sword', 'a rusty sword'),  Item('elf', 'He thinks anything you say is offensive towards elves')]
# 

#
# Main
#


# Make a new player object that is currently in the 'outside' room.

user_player = Player(input('Please enter your username: '), room['outside'])

print(user_player.name)
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

def list_room_items():
    if user_player.current_room.items == []: 
            print(f'There are no items in {user_player.current_room.name}')
    else:
            print('Items in room: ', user_player.current_room.get_items())
    
cmd = ''
while cmd != 'q': 

    print(user_player.current_room.name, user_player.current_room.description)
    list_room_items()
    cmd = input("You can move using this game! Press 'n' to travel north, 's' to travel south, 'w' to travel west, 'e' to travel east and 'q' to quit.")    
    if cmd == 'q': 
        print('Goodbye')
    elif cmd in ('n', 's', 'e', 'w'): 
        user_player.travel(cmd)
        print(user_player.current_room.name, user_player.current_room.description)
        list_room_items()
    
    elif len(cmd) >= 2: 
        action = cmd.split()
        if action[0] in ('take', 'pickup', 'remove'):
            for item in user_player.current_room.items: 
                if action[1] == item.name:  
                    user_player.pickupItem(item)
        elif action[0] in ('drop', 'leave', 'add'): 
             for item in user_player.items: 
                if action[1] == item.name:  
                    user_player.dropItem(item)