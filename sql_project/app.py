import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.execute('select * from  sample ')
a = cursor.fetchall();
print(a)
connection.commit()
connection.close()


# create table sample(id integer, name text)