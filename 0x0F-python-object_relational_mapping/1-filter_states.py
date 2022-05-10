#!/usr/bin/python3
"""
Filterates
"""

if __name__ == "__main__":
    import MySQLdb
    import sys


    username = argv[1]
    password = argv[2]
    d_name = argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password, db=d_name)
    cu = conn.cursor()
    cu.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cu.fetchall()

    for eachRow in rows:
        if eachRow[1][0] == 'N':
            print(eachRow)
    cu.close()
    conn.close()
