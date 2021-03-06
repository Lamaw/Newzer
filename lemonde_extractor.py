# -*- coding: utf-8 -*-

"""
This page defines the Implementation of an analyzer for "www.lemonde.fr"
"""
from HTMLParser import HTMLParser

from Isite_extractor import ISiteExtractor

class LeMondeExtractor(ISiteExtractor):
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
        # Use HTML parser to extract appropriates urls
        lemonde_parser = LeMondeHTMLParser()
        lemonde_parser.feed(news_feed_webpage)
        partial_url_list = lemonde_parser.links


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
        lemonde_parser = LeMondeHTMLParser()
        lemonde_parser.feed(article_webpage)
        return lemonde_parser.article_data

    def get_article_category(self, article_webpage):
        """
        Extract the category of the article from the raw webpage
        :type article_webpage: str
        :param article_webpage: The webpage containing the article to extract
        :return type: str
        :return: the category from the article on a web page (e.g: sport, economy, politics, etc...)
        """
        lemonde_parser = LeMondeHTMLParser()
        lemonde_parser.feed(article_webpage)
        return lemonde_parser.category

    def get_article_author(self, article_webpage):
        """
        Extract the author of the article from the raw webpage
        :type article_webpage: str
        :param article_webpage: The webpage containing the article to extract
        :return type: str
        :return: the author name from the article on a web page
        """
        pass

class LeMondeHTMLParser(HTMLParser):
    """
    Class implementating some methods of the HTMLParser pytho lib, in order to acquire specific data for Lemonde website
    """

    def __init__(self):
        HTMLParser.__init__(self) # Parents constructor

        self.links = list() # The list of links from the news feed
        self.article_section = False # Flag for news feed parsing
        self.article_body = False # Flag for article text acquisition
        self.suspend_acquisition = False # flag to suspend data aqcuisition in the article body
        self.div_open_in_article_body = 0 # Number of open inside the main article div
        self.article_data = "" # store the text from the article
        self.category = "" # store the category of the article

    def handle_starttag(self, tag, attrs):
        """
        Method that manage tag opening in the HTML source code, to retrieve article content
        """
        try:
            if tag == "article": # Set flag for news feed parsing to true
                for name, value in attrs:
                    if name == 'class' and 'grid_12 alpha enrichi' in value:
                        self.article_section = True
            elif tag == "a" and self.article_section == True: # get a link from the news feed
                for name, value in attrs:
                    if name == "href":
                        if value not in self.links and "/journaliste/" not in value:
                            self.links.append(value)
            elif tag == "div" and not self.article_body: # Set flag from article body to true
                for name, value in attrs:
                    if name == 'id' and value == 'articleBody':
                        self.article_body = True
            elif tag == 'div' and self.article_body: # Increment number of open div in the main div of article (used to determine when the main article div is closed)
                self.div_open_in_article_body += 1
            elif tag == 'p' and self.article_body:  # Suspend aqcuisition for "lire aussi" section
                for name, value in attrs:
                    if name == 'class' and value == 'lire':
                        self.suspend_acquisition = True
            elif tag == 'section' and self.article_body:
                self.suspend_acquisition == True
            elif tag == 'iframe' and self.article_body:
                self.suspend_acquisition == True
            elif tag == 'body':
                for name, value in attrs:
                    if name == "class":
                        self.category = value
        except:
            pass

    def handle_endtag(self, tag):
        """
        Method that Manage tag ending, in order to determine when parsing get out of appropriate sections
        """
        try:
            if tag == "article":
                self.article_section = False
            elif tag == "div" and self.article_body and self.div_open_in_article_body == 0:
                self.article_body = False
            elif tag == 'div' and self.article_body and self.div_open_in_article_body > 0:
                self.div_open_in_article_body -= 1
            elif tag == 'p' and self.suspend_acquisition == True:
                self.suspend_acquisition == False
            elif tag == 'section' and self.suspend_acquisition == True:
                self.suspend_acquisition == False
            elif tag == 'iframe' and self.suspend_acquisition == True:
                self.suspend_acquisition == False

        except:
            pass

    def handle_data(self, data):
        """
        Store data when in right section of parsing
        """
        if self.article_body:
            if not self.suspend_acquisition:
                self.article_data += data