import sys

def ask_for_name():
    name = ''
    cond = False
    while cond == False:
        try:
            name = input('Enter your name: ')
            if len(name) > 1:
                cond = True
                return name
        except:
            cond = False
            input('Try again')
            
def inputNumber(tipo, mensaje):
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            if tipo == "entero":
                numero = int(numero)
            elif tipo == "real":
                numero = float(numero)
            else:
                print("Check! entero o real. Ctrl C!")
            validado = True
        except:
            print("Error. Debe ingresar un número", tipo)
    return numero


def validacion_entero(message='Ingrese un numero entero: ', min=0,max=sys.maxsize):
    """" Recibe un mensaje, minimo y maximo para el ingreso de un entero"""
    try:  
        numero = inputNumber('entero',message)
        while numero <= min or numero >= max:
            print(f'Numero entero mayor que {min} y menor que {max}')
            numero = inputNumber('entero', message)
        return numero
    except:
        return 'Error, argumento invalido'



if __name__ == '__main__':
    cant = validacion_entero('Ingrese la cantidad de personas a cargar: ')
    names = []
    names_guest = []
    file = 'guest.txt'
    with open(file) as reader:
        for line in reader.readlines():
            names_guest.append(line.strip().lower())

    print(names_guest)
        
    with open(file,'a') as reader:    # uso del append
        for i in range(cant):
            print(f'Ingrese el nombre {i}')
            name = ask_for_name()
            while name.lower() in names_guest: # si el nombre ya esta en el txt no lo agrega 
                name = input('Name already in database, try again: ')
            names.append(name)
            reader.write(f'{name}\n')
    print(names)

        

         