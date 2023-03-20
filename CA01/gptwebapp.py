'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py
On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request,redirect,url_for,Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

@app.route('/')
def index():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1>Team Page</h1>
        <a href="{url_for('team')}">Info about team members</a>
        <h1>About Page</h1>
        <a href="{url_for('about')}">Info about this program and each GPT method</a>
        <h1>GPT Demo</h1>
        <a href="{url_for('gptdemo')}">Ask questions to GPT</a>
        <h1>Shakesperean Sonnet</h1>
        <a href="{url_for('shakeSonnet')}">Turn a prompt into a Shakespearean Sonnet</a>
        <h1>Convert Python Code to MATLAB Code</h1>
        <a href="{url_for('py_to_mat')}">Converts your python code into MATLAB code</a>
        <h1>Code Comments</h1>
        <a href="{url_for('code_comments')}">Automatically comments your code</a>
        <h1>Recipe Creation</h1>
        <a href="{url_for('recipe')}">Generate recipes</a>
    '''
    
@app.route('/team')
def team():
    return('''
    <h1>Team Page</h1>
    <b>Lucas Dia</b>
    <p>I am a sophomore, I am on the XC and TF team. I am majoring in CS, ECON, and BUS. I created the Shakespearean Sonnet method, and the shakeSonnet method.
    I also contributed to the index page and made the Team page, and about page. </p>
    <br>
    <b>Nathan Weiss</b>
    <p>I'm a sophomore studying Applied Math and Computer Science here at Brandeis. I created generateMATLAB 
    in gpt.py and py_to_mat in gptwebapp.py and contributed to the Index page and this page. </p>
    <br>
    <b>Simon Goode</b>
    <p>I'm a sophomore studying Applied Math and Economics, and I love going to the gym. I created comment_code 
    in gpt.py and code_comments in gptwebapp.py, and contributed to the Index and Team pages. </p>
    <br>
    <b>Evan Keleti</b>
    <p>I'm a freshman studying Computer Science and Physics. I created the recipe method in gpt.py and organized the index and about pages.</p>
    '''
    )

@app.route('/about')
def about():
    return f'''
    <h1>About Page</h1>
    <p>This program allows users to get GPT responses for specific prompts that each have an individual method and page. Each team member
    created a page that sends a form to the user and uses the input to prompt GPT for a response.</p>
    <div>
        <a href="{url_for('shakeSonnet')}"><b>Shakesperean Sonnet Method</b></a>
        <p>The Shakespearean Sonnet method takes the given prompt and asks GPT to write a shakespearean style sonnet using the prompt as inspiration. </p>
    </div>
    <div>
        <a href="{url_for('py_to_mat')}"><b>Python to MATLAB Method</b></a>
        <p>The Python to MATLAB method prompts the user to enter some python code that they want converted to MATLAB code. When that is input
        and the form is passed, we add some text to the front of their code saying that we want this code converted to MATLAB before passing
        to GPT. </p>
    </div>
    <div>
        <a href="{url_for('code_comments')}"><b>Code Commenting Method</b></a>
        <p>The Code Commenting Method takes code text as input and outputs the same code but with meaningful and pertinent documentation in
        the form of comments. </p>
    </div>
    <div>
        <a href="{url_for('recipe')}"><b>Recipe Creation Method</b></a>
        <p>The recipe creation asks gpt to generate a recipe to create the given prompt. This method is intended to be used for food recipes, but
        GPT will be asked to generate a recipe no matter what the input is.</p>
    </div>
    
    '''

@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>GPT Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
    
@app.route('/py_to_mat', methods=['GET', 'POST'])
def py_to_mat():
    '''takes a request form from the user and adds a prompt
    to the form, asking gpt to convert the following python
     code into matlab code'''
    
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.generateMATLAB(prompt)

        return f'''
        <h1> Convert Python to MATLAB </h1>
        {prompt}</pre>
        <hr>
        New Code in MATLAB:
        <pre style="border:thin solid black">{answer}</pre>
        <br>
        <a href={url_for('py_to_mat')}> Convert more code</a>
        <br>
        <a href={url_for('index')}> Index Page </a>
        '''
    else:
        return f'''
        <h1> Convert Python to MATLAB </h1>
        Enter a block of Python code below that you would like GPT to MATLAB code
        <form method="post">
            <textarea name ="prompt"></textarea>
            <p><input type=submit value="Get New Code">
        </form>
        <a href={url_for('index')}> Index Page </a>
        '''
        
@app.route('/shakeSonnet', methods=['GET', 'POST'])
def shakeSonnet():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.Shakesperean_Sonnet(prompt)
        return f'''
        <h1>Write a shakespearean sonnet using the prompt</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('shakeSonnet')}> make another query</a>
        '''
    else:
        return '''
        <h1>GPT Shakesperean Sonnet APP</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

@app.route('/code_comments', methods=['GET', 'POST'])
def code_comments():
    '''handle a get request by sending a form
       and a post request by returning the commented code response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.comment_code(prompt)
        return f'''
        <h1>Comment your code using the prompt</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('code_comments')}> make another query</a>
        '''
    else:
        return '''
        <h1>GPT Code Commenting App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    '''
    Handles a get request by sending a form prompting the user. Handles a post request by returning the response of asking GPT to give
    a recipe for the user input.
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.recipe(prompt)
        return f'''
        <h1>GPT Recipe Creation</h1>
        <p>Here is a recipe for {prompt}:</p>
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('recipe')}>make another query</a>
        '''
    else:
        return '''
        <h1>GPT Recipe Creation</h1>
        Enter your query below:
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)