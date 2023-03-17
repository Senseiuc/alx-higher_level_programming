#!/usr/bin/python3
"""
A script that lists all states
from the database hbtn_0e_0_usa
starting with N
"""
import MySQLdb
import sys

if __name__ == '__main__':
    arg = sys.argv
    db = MySQLdb.connect(host="localhost", port=3306, user=arg[1],
                         passwd=arg[2], db=arg[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")
    data = cur.fetchall()
    for i in data:
        print(i)
    cur.close()
    db.close()
