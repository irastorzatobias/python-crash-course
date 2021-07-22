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
    username = get_stored_username()
    if username: # If there is already a name stored
        return f'Hi {username} welcome back.'
    else: # If there isn't a name stored in usernames.json
        username = get_new_username()
        return f'Hi {username} first time.'
            
            
print(greet_user())
    

    
    