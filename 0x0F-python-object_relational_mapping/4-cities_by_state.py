#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
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

    sql = """SELECT cities.id, cities.name, states.name
             FROM states
             INNER JOIN cities ON states.id = cities.state_id
             ORDER BY cities.id ASC"""

    cur.execute(sql)

    row = cur.fetchall()

    for r in row:
        print(r)

    cur.close()
    db.close()
