from input_string import input_string
file = 'programming_pool.txt'

with open(file,'a') as reader:
    reason = ''
    while reason.lower() != 'fin':
        reason = input_string('\nWhy do u like python? (Answer below)\n')
        if reason.lower() != 'fin':
            reader.write(f'{reason}\n')




    