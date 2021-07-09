class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
    def get_name(self):
        """Gets the name of the dog"""
        return self.name
    
    
    def sit(self):
        """ Prints the dogs name + is now sitting"""
        return (f'{self.name} is now sitting.')
    
    
    def roll_over(self):
        """Simulate rolling over in response to a command"""
        return (f'{self.name} rolled over!')
    

luna = Dog('Luna',4)

print(luna.roll_over())
