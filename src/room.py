# Implement a class to hold room information. This should have name and
# description attributes.



class Room: 
    name = ''
    description = ''
    def __init__(self, name, description, n_to, s_to, w_to, e_to): 
        self.name = name 
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.w_to = w_to
        self.e_to = e_to



    def get_name(self): 
        return 'current room: ' + self.name
    
    def get_description(self): 
        return 'description: ' + self.description

