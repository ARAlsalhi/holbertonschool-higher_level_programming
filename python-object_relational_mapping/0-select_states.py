#!/usr/bin/python3
"""
0-select_states.py

Lists all states from the database passed as an argument.
Results are sorted by states.id in ascending order.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    db.close()
