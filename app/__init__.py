from flask import Flask #importing Flask class fro flask module
from .config import Config, DevConfig #getting config.py
from flask_bootstrap import Bootstrap #import the bootstrap class from flask_bootstrap


app = Flask(__name__)#Initializing the app

app.config.from_object(DevConfig)#setting up configuration
app.config.from_pyfile('config.py')#connects to the config.py file
bootstrap = Bootstrap(app) #initializing boostrap flask extension

from app import views #this will help in the creation of views
