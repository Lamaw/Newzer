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
        self.base_url = "http://www.lemonde.fr"

    def get_news_feed(self):
        """
        Get the news feed with newly published articles from the website home base_url
        :return type: str
        :return: the url on the news feed webpage
        """
        try:
            news_feed_url = self.base_url + "/actualite-en-continu/"
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
        try: # Use HTML parser to extract appropriates urls
            lemonde_parser = LeMondeHTMLParser()
            lemonde_parser.feed(news_feed_webpage)
            partial_url_list = lemonde_parser.links
        except:
            pass

        # add the base url of the website if not present in the article url
        for url in partial_url_list:
            if not 'http' in url:
                url_list.append(self.base_url + url)
            else:
                url_list.append(url)

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

    def __init__(self):
        HTMLParser.__init__(self)
        self.links = list()
        self.article_section = False

    def handle_starttag(self, tag, attrs):
        try:
            if tag == "article":
                for name, value in attrs:
                    if name == 'class' and 'grid_12 alpha enrichi' in value:
                        self.article_section = True
            elif tag == "a" and self.article_section == True:
                for name, value in attrs:
                    if name == "href":
                        if value not in self.links:
                            self.links.append(value)
        except:
            pass

    def handle_endtag(self, tag):
        try:
            if tag == "article":
                self.article_section = False
        except:
            pass