import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

courses = csv.DictReader(open("courses.csv"))
students = csv.DictReader(open("peeps.csv"))

f = "discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

command = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);"
c.execute(command)
command = "CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER PRIMARY KEY);"      #put SQL statement in this string
c.execute(command)    #run SQL statement

for i in courses:
    cm = 'INSERT INTO courses VALUES ("' + i["code"] + '", ' + i["mark"] + ", " + i["id"] + ");"
    c.execute(cm)

for i in students:
    cm = 'INSERT INTO peeps VALUES ("' + i["name"] + '", ' + i["age"] + ", " + i["id"] + ");"
    c.execute(cm)

#==========================================================
db.commit() #save changes
db.close()  #close database
