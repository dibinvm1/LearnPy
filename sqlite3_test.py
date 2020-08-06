import sqlite3

db = sqlite3.connect('D:\\Softwares\\SQLiteStudio-3.2.1\\test.db')

c = db.cursor()

#query = "select name,species from animals order by name COLLATE NOCASE;"

c.execute("insert into ordernames values('t1','t1')")

''' rows = c.fetchall()

#print(rows)

print("Animals")

for r in rows:
    print(" ",r[0])
'''
db.commit()
db.close()