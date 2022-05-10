#!/usr/bin/python3
"""All cities byate"""

if __name__ == "__main__":
    import MySQLdb
    import sys

     username = argv[1]
    password = argv[2]
    d_name = argv[3]
    state_name = argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password, db=d_name)
    cu = conn.cursor()
    query = "SELECT cities.name FROM cities INNER JOIN states ON \
             cities.state_id=states.id WHERE states.name = %(state_name)s "
    cu.execute(query, {'state_name': state_name})
    rows = cu.fetchall()
    l_cities = []

    for eachRow in rows:
        l_cities.append(eachRow[0])
    print(', '.join(l_cities))
    cu.close()
    conn.close()
