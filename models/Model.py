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

def get_book(ISBN):
    conn = my_database.mydb_manager
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM BOOKS WHERE ISBN={0}'.format(str(ISBN)))
    books = []
    for book in cursor:
        books.append(book)
    return books

def get_author(id):
    conn = my_database.mydb_manager
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM AUTHORS WHERE ID={0}'.format(id))
    author = []
    for authors in cursor:
        author.append(authors)
    return author


def add_new_book(ISBN, title, publisher, year, genre):
    conn = my_database.mydb_manager
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO BOOKS VALUES(\'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\')'
        .format(str(ISBN), str(title), str(publisher), str(year), str(genre)))
        conn.commit()
        return 200
        
    except mysql.connector.Error: 
        return 406