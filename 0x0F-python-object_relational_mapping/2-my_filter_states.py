#!/usr/bin/python3
"""
Filterates by user input
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    username = argv[1]
    password = argv[2]
    d_name = argv[3]
    state_name = argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password, db=d_name)
    cu = conn.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
    cu.execute(query.format(state_name))
    rows = cu.fetchall()

    for eachRow in rows:
        if eachRow[1] == state_name:
            print(eachRow)
    cu.close()
    conn.close()
