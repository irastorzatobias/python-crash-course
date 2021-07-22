import unittest

from name_function import get_formatted_name


class FormattedTest(unittest.TestCase):
     # Tests for formatted name
    
    def test_first_last_name(self):
        formatted_name = get_formatted_name('tobias','irastorza')
        self.assertEqual(formatted_name,'Tobias Irastorza')
    
    # Testing middle name 
    
    def test_middle_name(self):
        formatted_name = get_formatted_name('Tobias','Irastorza','tomas')
        self.assertEqual(formatted_name,'Tobias Tomas Irastorza')
    
    



if __name__ == '__main__':
    unittest.main() 
    