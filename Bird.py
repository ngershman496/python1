class Bird:

    #Attributes
    kingdom_class = 'bird'
    has_feathers = True
    
    #Initalizer
    def __init__ (self,name):
        self.name = name
        self.species = self.set_species()
        self.can_fly = self.set_can_fly()

    #functions
    def set_species(self):
        return input(f"\nWhat is the species of {self.name}: ")

    def set_can_fly(self):
        return input(f"Can a {self.species} fly: ")

    def introduction(self):
        print(f'My name is {self.name}\nHere are some facts about myself!')
        print(f'I am a {self.species}')
        print(f'I am a member of the {self.kingdom_class} class')
        if self.has_feathers:
            print('I also have feathers!')
        print(f'Can I fly? {self.can_fly}')
    

    

    
