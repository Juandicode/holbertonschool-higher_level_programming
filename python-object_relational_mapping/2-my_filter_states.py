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

    # Usamos format para crear la consulta con el valor de argv[4]
    query = (
        "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC"
        .format(argv[4])
    )
    cursor.execute(query)  # Ejecutamos la consulta
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
