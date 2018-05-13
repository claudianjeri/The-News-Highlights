from flask import render_template #this is for the creation of template files.
from app import app #import the app instance
from .request import get_sources#import the get_source function from request.py


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'News - One stop Mushene'

    business_news = get_sources('business')#create a variable that calss the get_sources function and pass in business as an argument.
    print(business_news)#passes the result from that function.

    return render_template('index.html', title = title, business = business_news) #it automatically searches for the template folder in the app folder.
