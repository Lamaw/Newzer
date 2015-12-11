# -*- coding: utf-8 -*-

import requests
import sys
import StringIO
import page_analyzer as pa


def give_IO_page_content(url):
	resp = requests.get(url)
	return StringIO.StringIO(resp.text)


if __name__ == '__main__':

	news_feed = give_IO_page_content('http://www.lemonde.fr/actualite-en-continu/')

	article_links = pa.get_article_links_from_feed(news_feed)

	articles = list()

	for link in article_links:
		articles.append(give_IO_page_content('http://www.lemonde.fr' + str(link)))

	with open("article.txt", "w+") as output_file:
		output_file.write(articles[0].read().encode('utf-8'))

	with open("article2.txt", "w+") as output_file:
		output_file.write(articles[1].read().encode('utf-8'))

