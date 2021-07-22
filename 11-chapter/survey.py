class AnonymousSurvey:
    def __init__(self,question):
        self.question = question
        self.responses = []
        
    def show_question(self):
        print(f'{self.question}')
    
    
    def store_response(self,response):
        self.responses.append(response)
    
    def show_results(self):
        """ Show all the responses that have been given"""
        print('Survey: ')
        for response in self.responses:
            print(f'{response}')
            



