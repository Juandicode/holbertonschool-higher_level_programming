#!/usr/bin/python3
'''
makinng a script
that lists all states that starts with N
'''
import MySQLdb
from sys import argv


i = "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY states.id"
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(i)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()