import unittest

from city_functions import get_city


class TestGetCity(unittest.TestCase):
    
    def test_get_city(self):
        """ Testing the method get city fom city_functions """
        rio_iv = get_city('argentina','rio cuarto')
        self.assertEqual(rio_iv,'Rio Cuarto, Argentina')
    
    def test_get_city_population(self):
        rio_iv = get_city('argentina','rio cuarto',population=50)
        self.assertEqual(rio_iv,'Rio Cuarto, Argentina - population 50')
        
    
        

if __name__ == '__main__':
    unittest.main()