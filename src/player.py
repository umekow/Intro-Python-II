# Write a class to hold player information, e.g. what room they are in
# currently.



class Player():

    def __init__(self, name, current_room): 
        self.name = name
        self.current_room = current_room

    def get_name(self): 
        return "Player's name: " + self.name

    def get_current_room(self):
        return "You are currently in : " + self.current_room.get_name()

    def change_room(self): 
        return ''

    