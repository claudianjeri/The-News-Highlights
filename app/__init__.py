from flask import Flask #importing Flask class fro flask module

app = Flask(__name__)#Initializing the app

app.config.from_object(DevConfig)#setting up configuration

from app import views #this will help in the creation of views
