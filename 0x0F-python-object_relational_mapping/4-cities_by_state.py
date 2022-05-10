#!/usr/bin/python3
"""
Cities byates
"""

import MySQLdb
import sys

if __name__ == '__main__':

    username = argv[1]
    password = argv[2]
    d_name = argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password, db=d_name)
    cu = conn.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities \
             INNER JOIN states ON cities.state_id=states.id \
             ORDER BY cities.id ASC"
    cu.execute(query)
    rows = cu.fetchall()

    for eachRow in rows:
        print(eachRow)
    cu.close()
    conn.close()
