import sqlite3


db=sqlite3.connect('baza.db')

c = db.cursor()

#c.execute("""CREATE TABLE articles (
#         title text,
#         full_text text,
#         views interger
#         avtor text
#)

#""")

c.execute("INSERT INTO articles VALUES('Facebook is cool', 'Facebook is realy cool', '200')")
 
c.execute("SELECT * FROM articles")
print(c.fetchall())
db.commit()

db.close()