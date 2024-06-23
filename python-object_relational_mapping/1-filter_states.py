#!/usr/bin/env python3
"""
A script that lists all states with a name starting with 'N' (upper N)
from the database hbtn_0e_0_usa.

This script connects to a MySQL database using the MySQLdb module,
retrieves all rows from the 'states' table where the name starts with 'N',
orders them by 'id' in ascending order.

Arguments: MySQL username, password, and database name.
"""

import MySQLdb
import sys

if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
