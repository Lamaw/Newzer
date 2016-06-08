# -*- coding: utf-8 -*-

import requests
import StringIO
from lemonde_extractor import LeMondeExtractor

class WebRequester():

    def __init__(self):
        pass

    def give_IO_page_content(self, url):
        resp = requests.get(url)
        return StringIO.StringIO(resp.text)

    def give_page_content(self, url):
        resp = requests.get(url)
        return resp.text

# if __name__ == '__main__':
    # req = WebRequester()

    # lemonde = LeMondeExtractor()
    # print "News feed url : "
    # print lemonde.get_news_feed()
    # news_feed_page = req.give_page_content(lemonde.get_news_feed())
    # print
    # print "Article url list : "
    # urls_article_list = lemonde.get_article_webpage_list(news_feed_page)
    # print urls_article_list
    # print
    # article_url = urls_article_list[0]
    # print
    # print "url of opened article : ", article_url
    # print "First article content : "
    # print lemonde.get_article_text(req.give_page_content(article_url))
