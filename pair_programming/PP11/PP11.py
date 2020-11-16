# Pairprogramming 11
# Coder: Jiahui Tang
# Sharer: Zeren Long
# Listener: Xingyu Liu, Yang Xiang, Gabin Ryu

import sqlite3

db = sqlite3.connect('test_db.sqlite') # Create a connection to the database
cursor = db.cursor() 
cursor.execute("DROP TABLE IF EXISTS candidates")

cursor.execute('''CREATE TABLE candidates (
               id INTEGER PRIMARY KEY NOT NULL, 
               first_name TEXT, 
               last_name TEXT, 
               middle_init TEXT, 
               party TEXT NOT NULL)''')

isFirstLine = True
with open('candidates.txt') as f:
    for line in f.readlines(): 
        if isFirstLine:
            isFirstLine = False
        else:
            line = line.rstrip('\n')
            fields = line.split('|')
            cursor.execute('''INSERT INTO candidates
                    (id, first_name, last_name, middle_init, party)
                    VALUES (?, ?, ?, ?, ?)''', 
                        (int(fields[0]), fields[1], fields[2], fields[3], fields[4]))
            db.commit()

cursor.execute("SELECT * FROM candidates")
all_rows = cursor.fetchall()
for row in all_rows:
    print(row)