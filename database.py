import sqlite3

def datas():
    conn = sqlite3.connect('movie.db')
    conn.execute("PRAGMA foreign_keys = 1")
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS customer (
                cid INTEGER PRIMARY KEY,
                c_name text,
                email_id text,
                phone_no text
            )""")

    c.execute(""" CREATE TABLE IF NOT EXISTS movie_data(
                m_id INTEGER PRIMARY KEY,
                m_name text,
                release_date text,
                director text,
                actors text,
                budget integer,
                duration int,
                rating int
            )""")
    
    c.execute(""" CREATE TABLE IF NOT EXISTS tickets(
                ticket_no INTEGER PRIMARY KEY,
                m_name text,
                price int,
                seat_no int,
                show_date text,
            )""")

    c.execute(""" CREATE TABLE IF NOT EXISTS booking(

                cid INTEGER PRIMARY KEY,
                ticket_no INTEGER PRIMARY KEY,
                show_date text,
                FOREIGN KEY(cid) REFERENCES customer(cid),
                FOREIGN KEY(ticket_no) REFERENCES tickets(ticket_no),
                FOREIGN KEY(show_date) REFERENCES tickets(show_date)

            )""")

    conn.commit()
    conn.close()


def addMovie(m_id,m_name,release_date,director,actors,budget,duration,rating):
    conn = sqlite3.connect('movie.db')
    c = conn.cursor()
    c.execute('INSERT INTO movie_data VALUES(?,?,?,?,?,?,?,?)',(m_id,m_name,release_date,director,actors,budget,duration,rating))
    conn.commit()
    conn.close()

def ViewMovieData():
    conn=sqlite3.connect("movie.db")    
    c=conn.cursor()
    c.execute("SELECT * FROM movie_data")
    rows=c.fetchall()
    conn.commit()
    conn.close()    
    return rows

def DeleteMovieRec(id):    
    conn=sqlite3.connect("movie.db")    
    c=conn.cursor()
    c.execute("DELETE FROM movie_data WHERE id=?", (id,))
    conn.commit()
    conn.close()

def addCustomerData(cid,c_name,email_id,phone_no):
    conn=sqlite3.connect("movie.db")    
    c=conn.cursor()
    c.execute('INSERT INTO customer VALUES(?,?,?,?)',(cid,c_name,email_id,phone_no))
    conn.commit()
    conn.close()

def addTickets(ticket_no,m_name,price,seat_no,show_date):
    conn=sqlite3.connect("movie.db")    
    c=conn.cursor()
    c.execute('INSERT INTO tickets VALUES(?,?,?,?,?)',(ticket_no,m_name,price,seat_no,show_date))
    conn.commit()
    conn.close()


def addBooking(cid,ticket_no,show_date):
    conn=sqlite3.connect("movie.db")    
    c=conn.cursor()
    c.execute('INSERT INTO booking VALUES(?,?,?)',(cid,ticket_no,show_date))
    conn.commit()
    conn.close()

def deleteBooking(cid):
    conn=sqlite3.connect("movie.db")    
    c=conn.cursor()  
    c.execute('DELETE from booking WHERE cid=?',(cid,))
    conn.commit()
    conn.close()