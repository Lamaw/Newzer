# -*- coding: utf-8 -*-

"""
This page defines the Implementation of an analyzer for "www.lemonde.fr"
"""
from HTMLParser import HTMLParser

from Isite_extractor import ISite_Extractor

class LeMonde_Extractor(ISite_Extractor):
    """
    This class implements the Page analyzer interface for "lemonde.fr" website
    """

    def __init__(self):
        self.base_url = "http://www.lemonde.fr/"

    def get_news_feed(self):
        """
        Get the news feed with newly published articles from the website home base_url
        :return type: str
        :return: the url on the news feed webpage
        """
        try:
            news_feed_url = self.base_url + "actualite-en-continu/"
        except:
            news_feed_url = None
        return news_feed_url

    def get_article_webpage_list(self, news_feed_webpage):
        """
        Get the article webpage list from the webpage containing all the newly added articles.
        :type news_feed_webpage: str
        :param news_feed_webpage: the html page where articles' urls are
        :return type: list()
        :return: the list of urls for each article webpage
        """
        url_list = list()



        return url_list

    def get_article_text(self, article_webpage):
        """
        Extract the text of the article from the raw webpage
        :type article_webpage: str
        :param article_webpage: The webpage containing the article to extract
        :return type: str
        :return: the text from the article on a web page
        """
        pass

class LeMondeHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag