from lemonde_extractor import LeMondeExtractor
from database_manager import WebDataStorageManager
from web_client import WebRequester

req = WebRequester()

lemonde = LeMondeExtractor()
news_feed_page = req.give_page_content(lemonde.get_news_feed())
urls_article_list = lemonde.get_article_webpage_list(news_feed_page)

table_name = "ARTICLE"

db = WebDataStorageManager()
db.create_table(table_name, 'Source','Url','Content')

article_stored = 0
for article_url in urls_article_list:
    try:
        article_content = lemonde.get_article_text(req.give_page_content(article_url))
        db.insert_data(table_name, 'Le Monde',article_url, article_content)
        article_stored += 1
        print "Article stored : ", article_stored
    except Exception as e:
        print "Error in : ", article_url
        print e

# db.cursor.execute("SELECT Url FROM ARTICLE WHERE Source='Le Monde'")

# for each in db.cursor.fetchall():
#     print
#     print
#     print each
#     print