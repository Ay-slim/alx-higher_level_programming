#!/usr/bin/python3
"""A module to make a mysql DB call using the MySQLdb library"""
import MySQLdb
import sys


def db_call(u, pw, db, n):
    """
    Use MySQLdb to run a query on the holberton DB for entries matching arg
    but ensure SQL injections are not possible
    """
    db = MySQLdb.connect(user=u, passwd=pw, db=db, host="localhost", port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (n,))
    for row in cur.fetchall():
        print(row)


if __name__ == "__main__":
    db_call(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
