
from page_233 import User
class Privileges:
    def __init__(self, privileges=[]):
       self.privileges = privileges 
    
    
    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")

        
    def add_privileges(self, privilege):
        """" Adds a privilege for the admin"""
        self.privileges.append(privilege)


class Admin(User):
    """ Class to define a user with privileges """
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        # Initializes an empty set of privileges
        self.privileges = Privileges()
        
        
    
    


my_admin = Admin('Tobias', 'Irastorza') 
my_admin.describe_user()
print("\nAdding privileges...")
privilegios = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]


# Modificando privilegios dentro de la clase privilegios
my_admin.privileges.privileges  = privilegios
# Accedo al metodo dentro de la instancia creada en mi clase Admin
my_admin.privileges.show_privileges()


