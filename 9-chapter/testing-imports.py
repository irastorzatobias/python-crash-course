from restaurant import Restaurant
from admin_privileges_user import User, Admin, Privileges
from admin import Admin as administrador

tobias = Admin('Tobias','Irastorza')
privilegios = ['borrar', 'agregar','modificar css','modificar html']
tobias.privileges.privileges = privilegios

# tobias.privileges.show_privileges()
mandriles = Restaurant('Mandriles','junk food')

lautaro = administrador('Lautaro','Irastorza')
lautaro.privileges.show_privileges()

 
 
 
 
 
 