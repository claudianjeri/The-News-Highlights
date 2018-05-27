from app import app #importing app instance
import urllib.request 
import json #imported urllib.request module that will help in the creation of the API URL and sends a request to json modules
from .models import Source
from .models import Articles
import certifi

Source = news.Source

Article = articles.Articles

api_key = None
base_url = None#getting the base url 
articles_url = None
def configure_request(app):
    global api_key,base_url, articles_url
api_key = app.config['NEWS_API_KEY']#we get the api key for the requests.
base_url = app.config['SOURCE_API_BASE_URL']#getting the base url 
articles_url = app.config['ARTICLES_API_BASE_URL']

def get_sources(category):#this function takes category as an argument
    '''
    Function that gets the json response to our url request

    '''

    get_source_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_source_url, cafile=certifi.where()) as url:#sends the request as a url
        get_source_data = url.read()#read() reads the response and stores it.
        get_source_response = json.loads(get_source_data)#the response is in JSON format, this line converts it to a python dictionary.

        source_results = None

        if get_source_response['sources']:#checks if the response has any results
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)

    return source_results #then we return the list.

def process_results(sources_list):#takes in a list of dictionaries
    
    '''
    function that processes the news results and transform them to a list of objects
    Args:
        source_list: A list of dictionaries that contain news details
    Returns:
        source_results: Alist of news source objects
    '''
    source_results = [] #create an empty list. It will store source objects
    for source_item in sources_list: #loops through the list of dictionary and passes in keys using the get method, so that I can get the values.
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        if id:#checks if the object has an id. If it does, its added to the list.
            source_object = Source(id,name,description,url,category,language,country)
            source_results.append(source_object)

    return source_results

def get_articles(id):
    '''
    Function that gets the json response to url request
    '''
    get_article_news_url = articles_url.format(id,api_key)
    with urllib.request.urlopen(get_article_news_url, cafile=certifi.where()) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)

    return article_results

def process_articles(articles_list):
    '''
    process the dictionary and output a list of objects
    '''
    article_results = []
    source_dictionary = {}
    for result in articles_list:
        source_id = result ['source']
        source_dictionary['id'] = source_id['id']
        source_dictionary['name'] = source_id['name']
        id = source_dictionary['id']
        name = source_dictionary['name']
        
        author = result.get('author')
        title = result.get('title')
        description = result.get('description')
        url = result.get('url')
        urlToImage = result.get('urlToImage')
        publishedAt = result.get('publishedAt')

        if urlToImage:
            print (id)
            article_object = Article(id,name,author,title,description,url,urlToImage,publishedAt)

            article_results.append(article_object)

    return article_results

