# -*- coding: utf-8 -*-

"""
This page defines the Interface for a web page analyzer in this app.
It stores top level functions that should be implemented for all websites supported by Newzer
"""

class IPage_Analyzer():
    """
    This class is the standard interface of a page analyzer, for any website supported by this app.
    e.g. A class NewYorkTime_Analyzer will inherit from this interface and implement it as needed.
    """

    def get_news_feed(base_url):
        """
        Get the news feed with newly published articles from the website home base_url
        :type base_url: str
        :param base_url: The home url of the given website.  e.g. "http://www.nytimes.com/"
        """
        pass

    def get_article_webpage_list(news_feed_webpage):
        """
        Get the article webpage list from the webpage containing all the newly added articles.
        :type news_feed_webpage: str
        :param news_feed_webpage: 
        """
        pass