# Implement a class to hold room information. This should have name and
# description attributes.



class Room: 
    def __init__(self, name, description, list = None): 
        self.name = name 
        self.description = description
        if list == None: 
            list = []
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None




    def get_name(self): 
        return 'current room: ' + self.name
    
    def get_description(self): 
        return 'description: ' + self.description

