import unittest #import unittest module 
from app.models import news #import the news module

Source = news.Source #getting news class 

class NewsTest(unittest.Testcase): #created a subclass and defined the test case.

    def setUp(self):
        #This should be run before every test.
        #defining our parameters from news.py

        self.new_news = Source("abc-news,ABC News, Your trusted source for breaking news,http://abcnews.go.com, general, en, us")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, Source))


