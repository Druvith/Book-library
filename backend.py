import sqlite3                        #import sqlite3 lib


def connect():                              #creating the function connect
    conn = sqlite3.connect("books.db")      #creating a connection to books.db database
    cur = conn.cursor()                     #connecting the con to the cursor
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text,author text,year integer,isbn integer)")     #executing thr table
    conn.commit()                           #commiting the changes
    conn.close()                            #closing the connection


def insert(title,author,year,isbn):         #creating the insert function
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():                                #creating the view function
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")   
    rows = cur.fetchall()                  #fetching all the rows
    conn.close()
    return rows


def search(title=" ",author=" ",year=" ",isbn=" "):             #creating the function search
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",(title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows 


def delete(id):                                               #creating the delete function
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?",(id,))  
    conn.commit()
    conn.close() 

def update(id,title,author,year,isbn):                         #UPDATE function
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?,author = ?,year = ?,isbn = ? WHERE id = ?",(title,author,year,isbn,id))  
    conn.commit()
    conn.close()      


connect()


#insert(title = "Rich dad poor dad",author = "Robert kiyosaki",year = "1997",isbn = "2819821")
print(search()) 
