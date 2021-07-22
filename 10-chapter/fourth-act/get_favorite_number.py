import json
from set_favorite_number import set_favorite_number

def get_favorite_number():
    """" Gets user favorite number if it exists, if not, promps it."""
    filename = 'fav_number.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        number = set_favorite_number()
        return f'I will remember your number next time'
    else:
        return f'Your favorite number is {number}'

    
print(get_favorite_number())