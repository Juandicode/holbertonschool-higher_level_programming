#!/usr/bin/python3
'''
makinng a script
that searches for a word in a table
of a given database
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    exe = "SELECT * FROM states WHERE BINARY name='{:s}'\
        ORDER BY states.id".format(argv[4])
    cur.execute(exe)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
