def input_birthday():
    """" Funcion para ingresar fecha de cumpleaños en formato ddmmaaaa sin separadores"""
    birthday = ''
    cond = False
    while cond == False:
        try:
            birthday = input('Enter your birthday, in the form ddmmaaaa: ')
            if len(birthday) != 8:
                cond = False
            else:
                birthday_num = int(birthday)
                if birthday_num > 0:
                    cond = True
                    return birthday        
                else:
                    cond = False
        except:
            cond = False
            print('Try again')
            

if __name__ == '__main__':
    file = 'pi_million_digits.txt'
    my_birthday = input_birthday()

    with open(file, 'r') as reader:
        result = ''
        for line in reader.readlines():
            result += line.strip()


    if my_birthday in result:
        print('Your birthday is in the first one million digits of pi')
    else:
        print('Your birthday is not in the first million digits of pi')




    
        
    