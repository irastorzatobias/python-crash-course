import unittest

from class_employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Tobias', 'Irastorza', 50000)
    
    def test_give_default_raise(self):
        """" Test that a default raise works correctly. """
        self.employee.give_raise() # realizo el aumento
        self.assertEqual(self.employee.anual_salary, 55000) # comparo si el aumento es igual a mi simulacion del aumento
        
    def test_give_custom_raise(self):
        """ Test that a custom raise works correctly """
        self.employee.anual_salary += 2000
        self.assertEqual(self.employee.anual_salary, 52000)


if __name__ == '__main__':
    unittest.main()
    