
## Exercise number 8-12 8-13

def make_sandwich(*toppings):
    """ Make a sandwich"""
    sandwich = {
        'toppings': []
    }
    for t in toppings:
        sandwich['toppings'].append(t.title())
    return sandwich


def make_car(manufacturer, model, **car):
    """" Make a car """
    car['manufacturer'] = manufacturer.title()
    car['model'] = model.title()
    return car





