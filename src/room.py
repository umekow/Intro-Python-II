# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items
        if self.items == None:
            self.items = []
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

    def remove_item(self, item):
        self.items.remove(item)

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return [x.name for x in self.items]
