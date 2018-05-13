from app import app #importing app instance
import urllib.request, json #imported urllib.request module that will help in the creation of the API URL and sends a request to json modules
from .models import news

Source = news.Source

api_key = app.config['NEWS_API_KEY']#we get the api key for the requests.
base_url = app.config['SOURCE_API_BASE_URL']#getting the base url 

# def get_sources(category):
