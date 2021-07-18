from guest import ask_for_name

if __name__ == '__main__':
    name = ''
    names = []
    file = 'guest_book.txt'
    names_guest = []
    
    with open(file) as reader:
        for line in reader.readlines():
            names_guest.append(line.strip().lower())

    with open(file, 'a') as reader:           
        while name.lower() != 'fin':
            name = input('Nombre (fin para finalizar la carga): ')
            while name.lower() in names_guest:
                name = input('Nombre existente, intente nuevamente: ')
            names.append([])
            if name.lower() not in 'fin':
                print(f'Hi {name}\n')
                reader.write(f'{name}\n')


