import unittest #import unittest module 
from .models import Source #import the news module

Source = news.Source #getting news class 

class NewsTest(unittest.Testcase): #created a subclass and defined the test case.

    def setUp(self):
        #This should be run before every test.
        #defining our parameters from news.py

        self.new_news = Source()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, Source))

if __name__ == '__main__':
    unittest.main()
