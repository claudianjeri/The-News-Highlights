from flask import render_template #this is for the creation of template files.
from app import app #import the app instance

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'News - One stop Mushene'

    return render_template('index.html', title = title) #it automatically searches for the template folder in the app folder.
