import unittest #import unittest module 
from .models import Articles #import the news module

Articles = news.Source #getting news class 

class ArticlesTest(unittest.Testcase): #created a subclass and defined the test case.

    def setUp(self):
        #This should be run before every test.
        #defining our parameters from news.py

        self.new_article = Articles("CNN", "null", "Haley: Gaza violence unrelated to embassy move - CNN Video", "US Ambassador to the United Nations Nikki Haley says moving the US Embassy to Jerusalem.", http://us.cnn.com/videos/world/2018/05/15/nikki-haley-unsc-jerusalem-embassy-sot.cnn, https://cdn.cnn.com/cnnnext/dam/assets/180515105038-nikki-haley-unsc-05152018-super-tease.jpg, 2018-05-15T15:37:46.7940666Z )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))

if __name__ == '__main__':
    unittest.main()