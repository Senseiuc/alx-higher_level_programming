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
    cur.execute("""SELECT cities.id, cities.name
                FROM cities JOIN states ON cities.state_id=states.id
                WHERE states.name LIKE BINARY %(state)s
                ORDER BY cities.id ASC""", {'state': arg[4]})
    data = cur.fetchall()
    if data:
        print(", ".join([d[1] for d in data]))
    cur.close()
    db.close()
