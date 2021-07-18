files = ['cats.txt', 'dogs.txt']

for file in files:
    names = []
    try:
        if 'cat' in file:
            with open(file) as f:
                print(f'Names of cats: ')
                for e in f.readlines():
                    print(f'{e.rstrip()}')
        elif 'dog' in file:
            with open(file) as f:
                print(f'\nNames of dogs: ')
                for e in f.readlines():
                    print(f'{e.rstrip()}')
    except:
        pass
        # print(f'\n{file} no existe en el directorio!')
        



        

