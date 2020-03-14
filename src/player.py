# Write a class to hold player information, e.g. what room they are in
# currently.



class Player():

    def __init__(self, name, current_room, items = None): 
        self.name = name
        self.current_room = current_room
        self.items = items
        if self.items == None: 
            self.items = []
        self.health = 100


    def travel(self, direction): 
        if getattr(self.current_room, f'{direction}_to'): 
            self.current_room = getattr(self.current_room, f'{direction}_to')
        else: 
            print('\n\n*Thump!!!*\n')
            print('You walked into a wall. Pick another direction\n\n')

    def get_items(self): 
        return [x.name for x in self.items]


    def dropItem(self, item):
        if item in self.items: 
            self.items.remove(item)
            print(f'You dropped off {item.name} in {self.current_room.name}.\n')
            self.current_room.add_item(item)
            print('Your inventory: ', self.get_items())
            print(f'Items left in room: ', self.current_room.get_items())
        else: 
            print('You are a liar! You do not possess this item')

    def pickupItem(self, item): 
        
        if item in self.current_room.items: 
            self.items.append(item)
            print(f'You picked up {item.name} from {self.current_room.name}.\n')
            print(f'{item.name}\'s description: {item.description}. \n')
            self.current_room.remove_item(item)
            print('Your items: ', self.get_items())
            print('')
            print(f'Items left in { self.current_room.name}:', self.current_room.get_items())
            print('')
        else:
            print("This item is not located in this room \n")

    def takeReward(self, item): 
        self.items.append(item)
        print(f'Your items: ', self.get_items())

    