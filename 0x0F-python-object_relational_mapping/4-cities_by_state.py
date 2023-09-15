#!/usr/bin/python3
"""A module to make a mysql DB call using the MySQLdb library"""
import MySQLdb
import sys


def db_call(u, pw, db):
    """
    Use MySQLdb to fetch all cities from hbtn_0e_4_usa
    """
    db = MySQLdb.connect(user=u, passwd=pw, db=db, host="localhost", port=3306)
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities c \
                JOIN states s ON c.state_id=s.id ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)


if __name__ == "__main__":
    db_call(sys.argv[1], sys.argv[2], sys.argv[3])
