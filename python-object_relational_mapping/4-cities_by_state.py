#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()

    # Usamos format para crear la consulta con el valor de argv[4]
    query = (
        "SELECT * FROM cities WHERE BINARY name = '{}' ORDER BY id ASC"
        .format(argv[4])
    )
    cursor.execute(query)  # Ejecutamos la consulta
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
