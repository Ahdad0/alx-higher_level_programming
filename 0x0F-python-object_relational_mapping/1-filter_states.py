#!/usr/bin/python3
"""
lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )

    cur = db.cursor()

    cur.execute(f"SELECT * FROM states ORDER BY id ASC")

    row = cur.fetchall()

    num = 0

    for r in row:
        if r[1][0] == 'N':
            print(r)

    cur.close()
    db.close()
