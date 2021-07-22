import unittest

from survey import AnonymousSurvey
""" Testing using the setUp method. """


class TestAnonymousSurvey(unittest.TestCase):
    """ Tests for the class Anonymous survey """
    
    def setUp(self):
        """ Create a survey and a set of responses for use in all test methods """    
        question = 'What lenguages did you first learned to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin'] # separado de self.my_survey.responses, se usa para comparar
    
    def test_store_single_response(self):
        """ Test that a single response is saved correctly"""
        
        self.my_survey.store_response(self.responses[0]) # accedo al metodo store response de mi instancia a traves de setUp
        self.assertIn(self.my_survey.responses[0],self.responses) # comparo si english esta en mi instancia de clase anteriormente declarada. 
     
    def test_store_three_responses(self):
        """ Test multiple responses """
        
        for l in self.responses: # lista de respuestas
            self.my_survey.store_response(l) # guardo el valor en mi instancia de clase
            
        for response in self.responses: # para cada respuesta en mi instancia de response
            self.assertIn(response, self.my_survey.responses) # chequeo si la respuesta esta en mi instancia de my_survey
            
if __name__ == "__main__":
    unittest.main()
        
        