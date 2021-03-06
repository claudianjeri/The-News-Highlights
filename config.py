import os

class Config:
    #my api key.
    NEWS_API_KEY = '8a48624dfbfc41d8a7009f960cccd473'
    SECRET_KEY = 'nsdbbdkjsbnjrbwucsjanvrbvuhcurwhcnerhicewi'
    #my source base url
    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?&category={}&language=en&apiKey=8a48624dfbfc41d8a7009f960cccd473'

    #my articles base url
    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=8a48624dfbfc41d8a7009f960cccd473'

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}