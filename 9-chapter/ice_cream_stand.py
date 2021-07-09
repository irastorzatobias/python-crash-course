from page_233 import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Limon','Crema del cielo','Vainilla', 'Chocolate']
        
    
    def show_flavors(self):
        print('-- FLAVORS --')
        for e in self.flavors:
            print(f'- {e.title()}')
            
            


grido = IceCreamStand('Grido', 'ice-cream')
print(grido.show_flavors())