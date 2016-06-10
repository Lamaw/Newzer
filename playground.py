from lemonde_extractor import LeMondeExtractor
from database_manager import WebDataStorageManager
from web_client import WebRequester

# Configuration
table_name = "ARTICLE"


# Instances creation
req = WebRequester()
lemonde = LeMondeExtractor()
db = WebDataStorageManager()

# get articles url list from websites
news_feed_page = req.give_page_content(lemonde.get_news_feed())
urls_article_list = lemonde.get_article_webpage_list(news_feed_page)

# Database initialisation
try:
    db.create_table(table_name, 'Source','Url','Content')
    print "Table "+ table_name + " created."
except:
    print "Table already existing, no creation needed."

# get urls of already stored artist
stored_url_list = db.get_stored_content_from_column(table_name, "Url")


# remove article from list if already present if database. It must not be downloaded again
for stored_url in stored_url_list:
    if stored_url[0] in urls_article_list:
        urls_article_list.remove(stored_url[0])

# articles aqcuisition process
article_stored = 0
if len(urls_article_list) == 0:
    print "No new article to download"
for article_url in urls_article_list:
    try:
        article_content = lemonde.get_article_text(req.give_page_content(article_url))
        db.insert_data(table_name, 'Le Monde',article_url, article_content)
        article_stored += 1
        print "Article stored : ", article_stored
    except Exception as e:
        print "Error in : ", article_url
        print "ERROR : ", e

# Display data from database

# db.cursor.execute("SELECT Url FROM ARTICLE WHERE Source='Le Monde'")

# for each in db.cursor.fetchall():
#     print
#     print
#     print each
#     print

# Post processing
db.kill_connect()