import mysql.connector





class my_database:
    mydb_manager = mysql.connector.connect(
        host='localhost',
        port='3360',
        user='db_manager',
        database='mydb',
        password='Admin1234')
    
    mydb_user = mysql.connector.connect(
        host='localhost',
        port='3360',
        user='web_user',
        # database='mydb', # asta n-are acces inca
        password='Admin123'
    )



def get_all_books():
    conn = my_database.mydb_manager
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM BOOKS')
    books = []
    for book in cursor:
        books.append(book)
    cursor.close()
    return books


def get_all_authors():
    conn = my_database.mydb_manager
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM AUTHORS')
    authors = []
    for author in cursor:
        authors.append(author)
    cursor.close()
    return authors


def get_book(ISBN):
    conn = my_database.mydb_manager
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM BOOKS WHERE ISBN={0}'.format(str(ISBN)))
    books = []
    for book in cursor:
        books.append(book)
    cursor.close()
    return books

def get_author(id):
    conn = my_database.mydb_manager
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM AUTHORS WHERE ID={0}'.format(id))
    author = []
    for authors in cursor:
        author.append(authors)
    cursor.close()
    return author


def add_new_book(ISBN, title, publisher, year, genre):
    conn = my_database.mydb_manager
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO BOOKS VALUES(\'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\')'
        .format(str(ISBN), str(title), str(publisher), str(year), str(genre)))
        conn.commit()
        cursor.close()
        return 200
        
    except mysql.connector.Error: 
        cursor.close()
        return 406


def replace_book(ISBN, title, publisher, year, genre):
    conn = my_database.mydb_manager
    cursor = conn.cursor()
    try:
        cursor.execute("""INSERT INTO BOOKS VALUES(\'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\')
         ON DUPLICATE KEY UPDATE
         ISBN=VALUES(ISBN), Title=VALUES(Title), Publisher=VALUES(Publisher), Year=VALUES(Year), Genre=VALUES(Genre);"""
        .format(str(ISBN), str(title), str(publisher), str(year), str(genre)))
        conn.commit()
        cursor.close()
        return 200
    except mysql.connector.Error:
        cursor.close()
        return 406

def delete_book(ISBN):
    conn = my_database.mydb_manager
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM BOOKS WHERE ISBN={}".format(ISBN))
        conn.commit()
        cursor.close()
        return 200
    except mysql.connector.Error:
        cursor.close()
        return 406


def get_book_author(ISBN):
    conn = my_database.mydb_manager
    books = []
    cursor = conn.cursor()
    try:
        cursor.execute("""SELECT b.Title, a.First_name, a.Last_name, ba.index FROM
        BOOKS b, AUTHORS a, BOOKS_TO_AUTHORS ba WHERE
        b.ISBN = ba.BOOKS_ISBN and a.ID = ba.AUTHORS_ID and b.ISBN = {};
        """.format(ISBN))
        for book in cursor:
            books.append(book)
        return books
    except mysql.connector.Error as err:
        print("Eroare: {}".format(err))
        return []


def search_with_pages(page=0, items_per_page=2, queries=None):
    conn = my_database.mydb_manager
    books = []
    cursor = conn.cursor()
    if(queries is None):
        try:
            cursor.execute("SELECT * FROM BOOKS")
            for book in cursor:
                books.append(book)
            return books[page*items_per_page:(page+1)*items_per_page]
        except mysql.connector.Error as err:
            print("Eroare: {}".format(err))
            return []
    else:
        try:
            string = "SELECT * FROM BOOKS WHERE "
            if(queries['title']):
                if('=' in string):
                    string = string + ' and TITLE=' + queries['title']
                else:
                    string = string + ' TITLE=' + queries['title']
            if(queries['genre']):
                if('=' in string):
                    string = string + ' and GENRE=' + queries['genre']
                else:
                    string = string + ' GENRE= ' + queries['genre']
            if(queries['year']):
                if('=' in string):
                    string = string + ' and YEAR= ' + queries['year']
                else:
                    string = string + ' GENRE= ' + queries['year']
            cursor.execute(string)
            for book in cursor:
                books.append(book)
            return books
        except mysql.connector.Error as err:
            print("Eroare: {}".format(err))
            return []            
            