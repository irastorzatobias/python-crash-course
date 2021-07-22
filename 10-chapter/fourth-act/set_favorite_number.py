import json
from os import system

def set_favorite_number():
    filename = 'fav_number.json'
    cond = False
    while cond == False:
        try:
            favNum = int(input('Enter your favorite number: '))
            cond = True
        except:
            system('cls')
            print('Error, not a number or invalid value')
        else:
            with open(filename, 'w') as f:
                json.dump(favNum, f)
            return favNum
