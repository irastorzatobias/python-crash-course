def adition():
    cond = False
    while cond == False:
        try:
            a = int(input('Enter your first number: '))
            b = int(input('Enter your second number: '))
        except:
            print('El valor que ingresaste no se puede convertir a entero')
        else:
            cond = True
            return f'El valor de la suma de esos dos numeros es: {a+b}'
    

 