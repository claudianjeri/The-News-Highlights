from flask import Flask #importing Flask class fro flask module

app = Flask(__name__)#Initializing the app

from app import views #this will help in the creation of views
