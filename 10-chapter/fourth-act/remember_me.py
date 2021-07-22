import json

def get_stored_username():
    """ Gets the name stored in usernames.json"""
    filename = 'usernames.json'
    try:
        with open(filename) as f:
            name = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return name


def get_new_username():
    """" Gets a new username and stores it in usernames.json"""
    filename = 'usernames.json'
    username = input('What is your name?: ')
    with open(filename,'w') as f:
        json.dump(username,f)
    return username

def greet_user():
    """ Greets the user stored in usernames.json"""
    correct = ''
    username = get_stored_username()
    if username: # If there is already a name stored
        while correct != 'n' and correct != 'y':
            correct = input(f'Are you {username}? (y/n): ')
            if correct.lower() == 'y': # If you are the user, waves at you
                return f'Hi {username} welcome back.'
            elif correct.lower() == 'n': # If you are not the user, ask for your name and stores it in usernames.json
                new_user = input('What is your name?: ')
                with open('usernames.json','w') as f:
                    json.dump(new_user, f)
                return f'Welcome {new_user}, first time'
    else: # If there isn't a name stored in usernames.json
        username = get_new_username()
        return f'Hi {username} first time.'
            
            
print(greet_user())