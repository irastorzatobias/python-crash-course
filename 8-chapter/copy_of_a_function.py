mensajes = ['hola', 'como', 'estas', 'pibe']
mensajesEnviados = []


def show_messages(messages, sentMessages):
    """" Elimina los mensajes de messages y los guarda en sentMessages"""
    while messages:
        currentMessage = messages.pop()
        sentMessages.append(currentMessage)
    return sentMessages


def show_people(**person):
    for k, v in person.items():
        print(k, v)

#

def build_profile(first, last, **user_info): # kwargs, key value args
    """ Build a dictionary containing everything we know about a user, **user_info create an empty dictionary named user_info.
    and allows to pass it whatever we want"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


print(build_profile('Tobias','Irastoza',sport='football',age=21))
