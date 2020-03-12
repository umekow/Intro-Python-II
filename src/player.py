# Write a class to hold player information, e.g. what room they are in
# currently.



class Player():

    def __init__(self, name, current_room, items = None): 
        self.name = name
        self.current_room = current_room
        self.items = items
        if self.items == None: 
            self.items = []


    def travel(self, direction): 
        if getattr(self.current_room, f'{direction}_to'): 
            self.current_room = getattr(self.current_room, f'{direction}_to')
        else: 
            print('\n\n*Thump!!!*\n')
            print('You walked into a wall. Pick another direction\n\n')

    