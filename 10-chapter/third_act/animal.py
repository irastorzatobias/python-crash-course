import json

file = 'animal.txt'


try:
    with open(file) as f:
        res_string = f.read().lower()
        word = input('Que palabra te gustaria encontrar en el texto?: ').lower()
        cant_word = res_string.count(word)
        if cant_word > 0:
            print(f'La cantidad de veces que aparece {word} es {cant_word}')
        else:
            print('No se encontro esa palabra')
except:
    print(f'{file} no está en el directorio')

