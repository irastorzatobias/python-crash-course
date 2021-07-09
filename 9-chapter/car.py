
class Car:
    """ A simple attempt to represent a car."""            
    
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer = 0
    
    
    def get_descriptive_name(self):
        """" Return a neatly formatted descriptive name"""
        long_name = f'{self.year} {self.manufacturer} {self.model}'
        print(long_name)
        
        
    def read_odometer(self):
        print(f'This car has {self.odometer} miles on it')
    
        
    def update_odometer(self, miles):
        """ Updates odometer, in case miles is less than the actual odometer, doesnt do it"""
        if (miles >= self.odometer):
            self.odometer = miles
        else:
            print('You cant rollback an odometer')
            
    def increment_odometer(self, miles):
        """In case you bought a car with a odometer > than 0, increment, not update it."""
        self.odometer += miles


# My new Car 

my_car = Car('Volkswagen', 'Gol', 2010)
# my_car.update_odometer(200)
# my_car.read_odometer()
# my_car.increment_odometer(100)
# my_car.read_odometer()
