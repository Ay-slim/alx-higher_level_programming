#!/usr/bin/python3
"""A module to make a mysql DB call using the MySQLdb library"""
import MySQLdb
import sys


def db_call(u, pw, db, state):
    """
    Use MySQLdb to fetch all cities from a given state
    """
    db = MySQLdb.connect(user=u, passwd=pw, db=db, host="localhost", port=3306)
    cur = db.cursor()
    cur.execute("SELECT c.name FROM cities c \
                JOIN states s ON c.state_id=s.id WHERE s.name=%s \
                ORDER BY c.id ASC", (state,))
    all_vals = cur.fetchall()
    val_str = ''
    for idx in range(len(all_vals)):
        if idx == len(all_vals) - 1:
            val_str += all_vals[idx][0]
        else:
            val_str += all_vals[idx][0] + ', '
    print(val_str)


if __name__ == "__main__":
    db_call(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
