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
        
        
class Admin(User):
    """ Class to define a user with privileges """
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        # Initializes an empty set of privileges
        self.privileges = Privileges()