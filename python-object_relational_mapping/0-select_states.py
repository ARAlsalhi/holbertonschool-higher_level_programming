#!/usr/bin/python3
"""
0-select_states.py

Lists all states from the database passed as an argument.
Results are sorted by states.id in ascending order.
"""
#!/usr/bin/python3
"""Lists all states from the given database."""

import sys
import MySQLdb


if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM states ORDER BY id ASC"
    )

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close()
