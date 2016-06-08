import sqlite3

class WebDataStorageManager():

    def __init__(self):
        self.connect = sqlite3.connect('articles.db')
        self.cursor = self.connect.cursor()

    def kill_connect(self):
        """
        Close the database connection
        """
        self.connect.close()

    def create_table(self, table_name, *args):
        """
        Create a table named "table_name" in the data base and having all slots given in *args
        :table_name type: str
        :table_name: the name of the data base new table
        :args type: list(str)
        :args: the columns of the table
        """
        table_slots = (",").join(args)
        self.cursor.execute("CREATE TABLE "+ table_name +" (" + table_slots +")")
        self.connect.commit()

    def insert_data(self, table_name, *args):
        """
        Create a new entrie in the table named "table_name" and having all entries given in *args
        :table_name type: str
        :table_name: the name of the table to enter new entry in
        :args type: list(str)
        :args: the new data to insert in the table
        """
        wrapped_args = list()
        for arg in args:
            wrapped_args.append("'"+ arg +"'")
        table_entries = (",").join(wrapped_args)
        statement = "INSERT INTO %s VALUES (" %(table_name)
        try:
            self.cursor.execute(statement + table_entries + ");" )
        except:
            print "Error found in : ", table_entries
        self.connect.commit()

