from database_manager import WebDataStorageManager


class StatFactory():
    """
    Class produce stats so they can be displayed
    """
    def __init__(self):
        self.db = WebDataStorageManager()

    def get_number_article_per_source(self, source):
        nb_article = None

        nb_article = len(self.db.get_stored_content_from_column("ARTICLE", "Url", Source=source))

        return nb_article

    def get_number_article_per_category(self, category):
        pass

    def get_number_article_per_source_and_category(self, source, category):
        pass

if __name__ == '__main__':
    factory = StatFactory()

    print "There is", factory.get_number_article_per_source("Le Monde") ,"articles from Le Monde in the Database"
