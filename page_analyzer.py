

def get_article_links_from_feed(lines_from_feed):
	"""
	Parse the html response of a news feed for article links extraction

	:type feed_html: str
	:param feed_html: The html page to parse for link extraction
	"""
	article_links = list()
	for line in lines_from_feed:
		if '<span class="nature_edito">' in line:
			fragments = line.split('"')
			for fragment in fragments:
				if 'a href=' in fragment:
					url_index =  fragments.index(fragment) + 1
					url = fragments[url_index]
					break
			article_links.append(url)

	return article_links
