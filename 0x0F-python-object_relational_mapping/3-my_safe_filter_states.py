#!/usr/bin/python3
"""SQL Injection..."""

import MySQLdb
import sys

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    d_name = argv[3]
    state_name = argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password, db=d_name)
    cu = conn.cursor()
    query = "SELECT * FROM states WHERE name = %(state_name)s ORDER BY id ASC"
    cu.execute(query, {'state_name': state_name})
    rows = cu.fetchall()

    for eachRow in rows:
        print(eachRow)
    cu.close()
    conn.close()
