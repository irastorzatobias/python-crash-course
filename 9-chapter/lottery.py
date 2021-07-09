from random import choice

def get_ticket(possibilities):
    """" Get a lottery ticket"""
    winning_ticket = []
    
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
    return winning_ticket
    
def check_ticket(played_ticket, winning_ticket):
    """" Chequea si mi ticket es igual al que se jugo"""
    for e in played_ticket: # chequea lo jugado en el ticket de la loteria|
        if e not in winning_ticket: # si el ticket de la loteria no coincide con el mio, devuelve falso
            return False
    return True # si no, verdadero

def make_random_ticket(possibilities):
    """ Genera un ticket aleatorio segun una lista de 10 numeros 5 letras que le demos"""
    random_ticket = []
    while len(random_ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in random_ticket:
            random_ticket.append(pulled_item)
    return random_ticket

serie = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
my_ticket = get_ticket(serie)
plays = 0
max_tries = 1000000
won = False

while not won: # mientras no gane
    new_ticket = make_random_ticket(serie) # genero un nuevo ticket|
    won = check_ticket(new_ticket, my_ticket) # lo comparo con el mio
    plays += 1 # sumo uno a jugadas
    if plays >= max_tries:
        break
    
if won:
    print(f'You won with the ticket {my_ticket}')
    print(f'Took you about {plays} tries')
    print(f'Congrats')
else:
    print(f'You lost with the ticket {my_ticket}')
    print(f'The winner ticket was {new_ticket}')


