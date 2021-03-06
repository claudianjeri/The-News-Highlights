from flask import render_template #this is for the creation of template files.
from . import main #import the app instance
from ..request import get_sources, get_articles#import the get_source function from request.py
from ..models import Source,Articles

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'News - One stop Mushene'

    business_news = get_sources('business')#create a variable that calss the get_sources function and pass in business as an argument.
    #passes the result from that function.
    sports_news = get_sources('sports')
    technology_news = get_sources('technology')
    entertainment_news = get_sources('entertainment')
    general_news = get_sources('general')
    health_news = get_sources('health') 
    science_news = get_sources('science')

    return render_template('index.html', title = title, business = business_news, health=health_news,science=science_news,sports = sports_news, technology = technology_news,entertainment = entertainment_news ,general = general_news) #it automatically searches for the template folder in the app folder.

@main.route('/news/<id>')
def news(id):
    '''
    view page function that returns the news articles and its data
    '''
    articles = get_articles(id)
    title = 'Home - Welcome to the best Online News Website'

    return render_template('news.html', articles=articles)