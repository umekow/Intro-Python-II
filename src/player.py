# Write a class to hold player information, e.g. what room they are in
# currently.



class Player():

    def __init__(self, name, current_room, items = None): 
        self.name = name
        self.current_room = current_room
        if items == None: 
            items = []


    def change_room(self, direction): 
        if getattr(self.current_room, f'{direction}_to'): 
            self.current_room = getattr(self.current_room, f'')

    