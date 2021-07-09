from car import Car


class Battery():
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    
    def describe_battery(self):
        return f'This car has a {self.battery_size}-kWh battery'

    
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100 or self.battery_size > 100:
            range = 315
        return (f'This car can go about {range} miles on a full charge')
    
    def upgrade_battery(self):
        if self.battery_size == 100:
            return 'Battery is on point'
        else:
            print('Upgrading battery')
            self.battery_size = 100
    
    
class ElectricCar(Car):
    """ Represent aspects of a car, specific to electric vehicules"""
    def __init__(self, manufacturer, model, year, battery):
        # Initialize attributes of the parents class
        super().__init__(manufacturer, model, year)
        self.battery = Battery(battery)
        
    
        
    

        

# tesla = ElectricCar('Tesla','Vergonha', 2020)

# print(tesla.get_descriptive_name())
# print(tesla.battery.describe_battery())
# print(tesla.battery.get_range())