#!/usr/bin/python3
"""A module to make a mysql DB call usint the MySQLdb library"""
import MySQLdb
import sys


def db_call(u, pw, db):
    """
    Use MySQLdb to run a query on the holberton DB
    """
    db = MySQLdb.connect(user=u, passwd=pw, db=db, host="localhost", port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)


if __name__ == "__main__":
    db_call(sys.argv[1], sys.argv[2], sys.argv[3])
