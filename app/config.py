class Config:
    #my api key.
    NEWS_API_KEY = '8a48624dfbfc41d8a7009f960cccd473'

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG = True

