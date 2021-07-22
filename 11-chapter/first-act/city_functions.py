def get_city(country, city, population=0):
    
    """ Return a single string of the form City, Country"""
    city_formatted = f'{city}, {country}'.title()
    if population: # optional population, no toma el 0 si no está, por eso funciona asi
        city_formatted = f'{city_formatted} - population {population}'
    return city_formatted



