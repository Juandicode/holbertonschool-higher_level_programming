#!/usr/bin/python3
'''
makinng a script that
gets information from a database
'''
import MySQLdb
from sys import argv


if __name__ == "__name__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    rows = cur.execute("SELECT * FROM states ORDER BY states.id")
    for row in rows:
        print(cur.fetchone())
    cur.close()
    db.close()