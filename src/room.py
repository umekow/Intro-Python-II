# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    name = ""
    description = ""

    def __init__(self, name, description):
        name = self.name
        description = self.description

    def get_name(self):
        return "current room: " + self.name

    def get_description(self):
        return "description: " + self.description
