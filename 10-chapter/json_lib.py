import json

numbers = [number for number in range(0,14) if number % 2 != 0]



with open('numbers.json') as f:
    result = json.load(f)
    print(result)
    



    