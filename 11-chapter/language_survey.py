from os import system

from survey import AnonymousSurvey


# Define a question, and make a survey
name = input('Hi, welcome to the survey, whats your name?: ')
file = 'survey_results.txt'
question = '-- How many languages do u know? --'
my_survey = AnonymousSurvey(question)

#Show the question
my_survey.show_question()
print('\n -- Enter q anytime to quit --')
while True:
    lenguage = input('Language: ')
    if lenguage.lower() == 'q':
        break
    else:
        my_survey.store_response(lenguage)

# Show the survey results
print(system('cls'))
print('Thank your for participating in the survey\n The results where: ')
with open(file,'a') as f:
    result_strng = ''
    for l in my_survey.responses: # cada respuesta en mi clase.
        print(f'- {l}')
        result_strng += f'{l},'
    f.write(f'{name},{result_strng[0:len(result_strng) - 1]}\n') # menos la ultima coma.


