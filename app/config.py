class Config:
    #my api key.
    NEWS_API_KEY = '8a48624dfbfc41d8a7009f960cccd473'

    #my source base url
    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?&apiKey=8a48624dfbfc41d8a7009f960cccd473'

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG = True

