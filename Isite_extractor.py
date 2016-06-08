# -*- coding: utf-8 -*-

"""
This page defines the Interface for a web page analyzer in this app.
It stores top level functions that should be implemented for all websites supported by Newzer
"""

class ISiteExtractor():
    """
    This class is the standard interface of a page analyzer, for any website supported by this app.
    e.g. A class NewYorkTime_Analyzer will inherit from this interface and implement it as needed.
    """

    def get_news_feed(base_url):
        """
        Get the news feed with newly published articles from the website home base_url
        :type base_url: str
        :param base_url: The home url of the given website.  e.g. "http://www.nytimes.com/"
        :return type: str
        :return: the url on the news feed webpage
        """
        pass

    def get_article_webpage_list(news_feed_webpage):
        """
        Get the article webpage list from the webpage containing all the newly added articles.
        :type news_feed_webpage: str
        :param news_feed_webpage: the html page where articles' urls are
        :return type: list()
        :return: the list of urls for each article webpage
        """
        pass

    def get_article_text(article_webpage):
        """
        Extract the text of the article from the raw webpage
        :type article_webpage: str
        :param article_webpage: The webpage containing the article to extract
        :return type: str
        :return: the text from the article on a web page
        """
        pass

    def get_article_category(article_webpage):
        """
        Extract the category of the article from the raw webpage
        :type article_webpage: str
        :param article_webpage: The webpage containing the article to extract
        :return type: str
        :return: the category from the article on a web page (e.g: sport, economy, politics, etc...)
        """
        pass

    def get_article_author(article_webpage):
        """
        Extract the author of the article from the raw webpage
        :type article_webpage: str
        :param article_webpage: The webpage containing the article to extract
        :return type: str
        :return: the author name from the article on a web page
        """
        pass