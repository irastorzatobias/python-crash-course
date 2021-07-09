class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """" Greets to the costumer, name of the restaurant and today's food """
        return(f'\nWelcome to {self.restaurant_name}\nToday we cook {self.cuisine_type} food\n')
        
    def open_restaurant(self):
        """ Tells if the restaurant is opened or not"""
        return ('The restaurant is open')

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    
    def describe_user(self):
        msg = f'Fullname: {self.first_name} {self.last_name}'
        print(msg)
        
    def greet_user(self):
        msg = f'Hello {self.first_name}'
        print(msg)



    


# Act 9.2 Three restaurants

# mandriles = Restaurant('Mandriles','asian')
# juniorB = Restaurant('Junior B','junk')
# tik = Restaurant('Tik', 'gourmet')
# tobias = User('Tobias', 'Irastorza')

# mandriles.describe_restaurant()
# juniorB.describe_restaurant()
# tik.describe_restaurant()

# Act 9-3 Class called User

# tobias.describe_user()







