from name_function import get_formatted_name

print('Enter q anytime to quit: ')
while True:
    first = input('Give me your first name: ')
    if first.lower() == 'q':
        break
    last = input('Give me your last name: ')
    if last.lower() == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f'Neatly formatted name: {formatted_name}')
    


