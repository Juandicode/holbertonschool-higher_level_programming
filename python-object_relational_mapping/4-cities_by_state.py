#!/usr/bin/python3
'''
makinng a script that
list all the cities in a state
'''
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    exe = "SELECT cities.id, cities.name, states.name FROM cities\
        JOIN states ON cities.state_id = states.id ORDER BY cities.id"
    cur.execute(exe)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
