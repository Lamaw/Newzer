# -*- coding: utf-8 -*-

import re

class ArticleAnalyzer():
    """
    Class doing the process of analyzing this article, decomposing it in order to store in database
    """

    def __init__(self, article):
        self.article = article
        self.word_list = list()

    def get_word_list_from_article(self):
        """
        get a text, and return a list of all words in it
        """
        word_list = self.article.split(" ")
        self.word_list = self.keep_only_letters(word_list)

    def keep_only_letters(self, word_list):
        """
        Remove all non letter charachter from each element of a list

        :type word_list: list(str)
        :param word_list: The list of word to remove all non-letters from
        """
        new_word_list = list()
        for word in word_list:
            word = re.sub(r'[^A-Za-z-]+','',word)
            new_word_list.append(word)

        return new_word_list
