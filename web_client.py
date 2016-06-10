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
