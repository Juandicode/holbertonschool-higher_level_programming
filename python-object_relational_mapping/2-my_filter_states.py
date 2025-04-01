#!/usr/bin/python3
"""
Lists all states from the database where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(
        query, (argv[4],)
    )  # Se pasa como tupla para evitar inyección SQL
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
