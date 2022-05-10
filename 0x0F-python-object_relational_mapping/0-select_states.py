#!/usr/bin/python3
"""
Get allates
"""

import MySQLdb
import sys

if __name__ == '__main__':

    username = argv[1]
    password = argv[2]
    d_name = argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password, db=d_name,
                           charset="utf8")

cu = conn.cursor()
cu.execute("SELECT * FROM states ORDER BY id ASC")
rows = cu.fetchall()
    for eachRow in rows:
        print(eachRow)
cu.close()
conn.close()
