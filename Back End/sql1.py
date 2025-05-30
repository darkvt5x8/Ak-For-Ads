import sqlite3
#con = sqlite3.connect('Back End/serv.db')

#con.close()


# Craete Tables in the database

#con = sqlite3.connect('serv.db')
#cursor = con.cursor()
#cursor.execute('CREATE TABLE serv(title TEXT, id INTEGER, description TEXT, image_url TEXT)')
#con.commit()
#con.close()

# Insert row into table

#con = sqlite3.connect('serv.db')
#cursor = con.cursor()
#cursor.execute('CREATE TABLE serv(title TEXT, id INTEGER, description TEXT, image_url TEXT)')
#cursor.execute("INSERT INTO serv(title,id,description,image_url) VALUES('Ads 1 Day', 25678491, 'https://image.png')")
#con.commit()
#con.close()


# Insert Multi Rows in Table

#con = sqlite3.connect('serv.db')
#cursor = con.cursor()

#services = [
#    ('Ad 1 Day', 25678491, 'Publish Your Ad 1 Day', 'https://image.png'),
#    ('Ad 3 Days', 25678493, 'Publish Your Ad 3 Days', 'https://image.png'),
#    ('Ad 7 Days', 25678497, 'Publish Your Ad 7 Days', 'https://image.png'),
#    ('Ad 15 Days', 256784915, 'Publish Your Ad 15 Days', 'https://image.png'),
#    ('Ad 30 Days', 256784930, 'Publish Your Ad 30 Days', 'https://image.png'),
#    ('Ad 60 Days', 256784960, 'Publish Your Ad 30 Days', 'https://image.png'),
#]



#cursor.execute('CREATE TABLE IF NOT EXISTS serv(title TEXT, id INTEGER, description TEXT, image_url TEXT)')
#c
#con.commit()
#con.close()





# Read Data from the table


#db = sqlite3.connect('Back End/serv.db')
#cur = db.cursor()


#services = [
#    ('Ad 1 Day', 25678491, 'Publish Your Ad 1 Day', 'https://image.png'),
#    ('Ad 3 Days', 25678493, 'Publish Your Ad 3 Days', 'https://image.png'),
#    ('Ad 7 Days', 25678497, 'Publish Your Ad 7 Days', 'https://image.png'),
#    ('Ad 15 Days', 256784915, 'Publish Your Ad 15 Days', 'https://image.png'),
#    ('Ad 30 Days', 256784930, 'Publish Your Ad 30 Days', 'https://image.png'),
#    ('Ad 60 Days', 256784960, 'Publish Your Ad 30 Days', 'https://image.png'),
#]

#cur.execute('CREATE TABLE IF NOT EXISTS serv(title TEXT, id INTEGER, description TEXT, image_url TEXT)')
#cur.executemany("INSERT INTO serv VALUES(?,?,?,?)", services)

#data = cur.execute("SELECT rowid,* FROM serv")

#for row in data:
#    print(row[0])

#db.commit()
#db.close()


# Read Data by Fetch

#db = sqlite3.connect('Back End/serv.db')
#cur = db.cursor()

#cur.execute("SELECT * FROM serv")
#data = cur.fetchall()

#for row in data:
#    print(row)

#db.commit()
#db.close()


            # Limit - Order by

#db = sqlite3.connect('Back End/serv.db')
#cur = db.cursor()

            #Normal
#cur.execute("SELECT rowid,* FROM serv ORDER BY id")

            #Reverse                        ASC (this is a default value)
#cur.execute("SELECT * FROM serv ORDER BY id DESC")


            #Limit
#cur.execute("SELECT rowid,* FROM serv ORDER BY id LIMIT 1")
#data = cur.fetchall()
#for row in data:
#    print(row)
#db.commit()
#db.close()



            #Where Condition
#db = sqlite3.connect('Back End/serv.db')
#cur = db.cursor()
                        # = , != , < , > , <= , >=   # AND , OR   # UPPER() , LOWER()

                        # LIKE = 2567849% , LIKE = 25678 , LIKE = %7849% 
                        # [ % ] = 1 or multi letter
                        # [ _ ] = 1 letter only
                        # BETWEEN 3 AND 30
                        # to get rows is not between 3 and 30 Use [ NOT BETWEEN ]
#cur.execute("SELECT * FROM serv WHERE id = 25678497 AND title = 'Ad 7 Days' ")

#print(cur.fetchall())


#db.commit()
#db.close()


            # Update Data
# 1 Entery to database
# 2 Edit Data
# 3 Read Data After Editing

#db = sqlite3.connect('Back End/serv.db')
#cur = db.cursor()
#cur.execute("UPDATE serv SET title = 'AD 1 Day' WHERE rowid = 1 ")

#cur.execute("SELECT * FROM serv")

#data = cur.fetchall() 

#for row in data:
#    print(row)

#db.commit()
#db.close()


            # Delet And Drop
#db = sqlite3.connect('Back End/serv.db')
#cur = db.cursor()
#cur.execute("DELETE FROM serv WHERE rowid = 8")


    # To Delet Table Use [ DROP TABLE table_name ]
#cur.execute("DROP TABLE serv")
#cur.execute("SELECT rowid,* FROM serv ORDER BY id")

#data = cur.fetchall() 

#for row in data:
#    print(row)

#db.commit()
#db.close()



            # IF NOT EXISTS - PRIMARY KEY
db = sqlite3.connect("Back End/serv.db")
cur = db.cursor()

    # To Create Table Without Problems Use
        # [ IF NOT EXISTS ]

cur.execute("""CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER
            )""")


    # Use [ NOT NULL ] to force enter data if null

cur.execute("INSERT INTO users(name, age) VALUES('Abdullah Khaled', 17)")
cur.execute("SELECT * FROM users")
data = cur.fetchall()

for row in data:
    print(row)

db.commit()
db.close()


            # This Course is Ended By Abdulalh Khaled with Abdulrahman Gamal [ Python & SQLite ]