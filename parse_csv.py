

import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('AppDev/UCLQuarterFinals.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS league')
conn.execute('DROP TABLE IF EXISTS locations')
print("table dropped successfully");

# create table again

conn.execute('CREATE TABLE league (ID INTEGER PRIMARY KEY AUTOINCREMENT, year INTEGER, name TEXT, code TEXT, league TEXT, round TEXT, decades TEXT, superliga TEXT)')
conn.execute('CREATE TABLE locations (ID INTEGER PRIMARY KEY AUTOINCREMENT, league_ID INTEGER, country TEXT, city TEXT, areacode TEXT, metropol TEXT,  FOREIGN KEY(league_ID) REFERENCES league(ID))')
# conn.execute('CREATE TABLE locations (ID INTEGER PRIMARY KEY AUTOINCREMENT, league_ID, country TEXT, league_year INTEGER, city TEXT, areacode TEXT, metropol TEXT,  FOREIGN KEY(league_ID) REFERENCES league(ID))')
print("table created successfully");

with open("AppDev/UCLQuarterFinals.csv", newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        year = int(row[0])
        name = row[2]
        code = row[1]
        league = row[4]
        round = row[3]
        decades = row[6]
        superliga = row[7]

        cur.execute('INSERT INTO league VALUES (NULL,?,?,?,?,?,?,?)', (year, name, code, league, round, decades, superliga))
        conn.commit()
print("data parsed successfully");


count = 1
with open('AppDev/UCLQuarterFinals.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)
        
        
        league_ID = count
        country = row[13]
        city = row[8]
        areacode = row[9]
        metropol = row[10]
        
        cur.execute('INSERT INTO locations VALUES (NULL,?,?,?,?,?)', (league_ID, country, city, areacode, metropol))
        count+=1
        conn.commit()
print("data parsed successfully");

conn.close()