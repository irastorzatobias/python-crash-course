# 9.4 Number served.
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    
    def describe_restaurant(self):
        """" Greets to the costumer, name of the restaurant and today's food """
        print(f'\nWelcome to {self.restaurant_name}')
        print(f'Today we cook {self.cuisine_type} food\n')
        
    
    def open_restaurant(self):
        """ Tells if the restaurant is opened or not"""
        print('The restaurant is open')


    def set_number_served(self, clients):
        if clients >= self.number_served:
            self.number_served = clients
        else:
            print('You cannot take clients')
    
    
    def increment_number_served(self, clients):
        self.number_served += clients

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attemps = 0
    
    
    def describe_user(self):
        msg = f'Fullname: {self.first_name} {self.last_name}'
        print(msg)
    
        
    def greet_user(self):
        msg = f'Hello {self.first_name}'
        print(msg)
        
        
    def increment_login_attemps(self):
        self.login_attemps += 1
        if self.login_attemps >= 3:
            self.reset_login_attemps()
            print('Max attemps reached.')


    def reset_login_attemps(self):
        self.login_attemps = 0
        

    

#mandriles = Restaurant('mandriles','junk')
#print(mandriles.number_served)
#mandriles.number_served = 10    
#mandriles.increment_number_served(15)
#print(mandriles.number_served)


#tobias = User('Tobias', 'Irastorza')
#tobias.increment_login_attemps()
#print(tobias.login_attemps)
#tobias.increment_login_attemps()
#print(tobias.login_attemps)
#tobias.increment_login_attemps()
#print(tobias.login_attemps)









            

