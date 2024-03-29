'''
Demo code for interacting with GPT-3 in Python.

To run this you need to 
* first visit openai.com and get an APIkey, 
* which you export into the environment as shown in the shell code below.
* next create a folder and put this file in the folder as gpt.py
* finally run the following commands in that folder

On Mac
% pip3 install openai
% export APIKEY="......."  # in bash
% python3 gpt.py

On Windows:
% pip install openai
% $env:APIKEY="....." # in powershell
% python gpt.py
'''
import openai


class GPT():
    ''' make queries to gpt from a given API '''
    def __init__(self,apikey):
        ''' store the apikey in an instance variable '''
        self.apikey=apikey
        # Set up the OpenAI API client
        openai.api_key = apikey #os.environ.get('APIKEY')

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"

    def getResponse(self,prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response
    

    #Simon Goode's request method
    def comment_code(self,prompt):
        ''' Generate GPT response that comments given code '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt="write comments for this code:\n"+prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )
        
        response = completion.choices[0].text
        return response
        
    #Nathan Weiss' request method
    def generateMATLAB(self,prompt):
        ''' Converts code that is given in python into MATLAB'''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt="Convert the following python code into MATLAB code: " + prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )
        
        response = completion.choices[0].text
        return response

    #Lucas Dia's request method
    def Shakesperean_Sonnet(self, prompt):
        '''Generate a GPT response'''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt="Write a shakesperean sonnet about the following: "+prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )
        
        response = completion.choices[0].text
        return response

    #Evan Keleti's request method
    def recipe(self, prompt):
        '''Generate cooking recipe using GPT'''
        return self.getResponse("Give me a recipe for: " + prompt)

if __name__=='__main__':
    '''
    '''
    import os
    g = GPT(os.environ.get("APIKEY"))
    print(g.getResponse("what does openai's GPT stand for?"))