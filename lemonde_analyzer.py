# -*- coding: utf-8 -*-

"""
This page defines the Implementation of an analyzer for "www.lemonde.fr"
"""

from Ipage_analyzer import IPage_Analyzer

class LeMonde_Analyzer(IPage_Analyzer):
    """
    This class implements the Page analyzer interface for "le monde.fr" website
    """

    def __init__():
        pass

    def get_news_feed(base_url):
        """
        Get the news feed with newly published articles from the website home base_url
        :type base_url: str
        :param base_url: The home url of the given website. 
        """
        pass

    def get_article_webpage_list(news_feed_webpage):
        """
        Get the article webpage list from the webpage containing all the newly added articles.
        :type news_feed_webpage: str
        :param news_feed_webpage: the html page where articles' urls are
        """
        pass

    def get_article_text(article_webpage):
        """
        Extract the text of the article from the raw webpage
        :type article_webpage: str
        :param article_webpage: The webpage containing the article to extract
        """
        pass