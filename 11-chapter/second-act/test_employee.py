import unittest

from class_employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Tobias', 'Irastorza', 50000)
    
    def test_give_default_raise(self):
        salario = self.employee.anual_salary + 5000 # variable salario que simula ya el aumento
        self.employee.give_raise() # realizo el aumento
        self.assertEqual(salario, self.employee.anual_salary) # comparo si el aumento es igual a mi simulacion del aumento
        
    def test_give_custom_raise(self):
        salario = self.employee.anual_salary + 2000
        self.employee.anual_salary += 2000
        self.assertEqual(salario, self.employee.anual_salary)


if __name__ == '__main__':
    unittest.main()
    