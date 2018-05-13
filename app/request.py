from app import app #importing app instance
import urllib.request, json #imported urllib.request module that will help in the creation of the API URL and sends a request to json modules
from .models import news

Source = news.Source

api_key = app.config['NEWS_API_KEY']#we get the api key for the requests.
base_url = app.config['SOURCE_API_BASE_URL']#getting the base url 

def get_sources(category):#this function takes category as an argument

     '''
    Function that gets the json response to our url request

    '''

    get_source_url = base_url.format(category,api_key) #.format method  on the base_url and pass in the movie category and the api_key
    #our final URL.
    with urllib.request.urlopen(get_source_url) as url:#sends the request as a url
        get_source_data = url.read()#read() reads the response and stores it.
        get_source_response = json.loads(get_source_data)#the response is in JSON format, this line converts it to a python dictionary.

        source_results = None

        if get_source_response['sources']:#checks if the response has any results
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)


    return source_results #then we return the list.