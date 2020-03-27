#!/usr/bin/env python3
""" Script to list all cities by state with
 an specific name from hbtn_0e_0_usa """
if __name__ == "__main__":
    import MySQLdb as sql
    import sys
    if len(sys.argv) == 5:
        db = sql.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
        c = db.cursor()
        c.execute("""
        SELECT cities.name FROM states
        LEFT JOIN cities ON states.id = cities.state_id
        WHERE states.name = %s ORDER BY cities.id""", (sys.argv[4],))
        names = []
        for row in c.fetchall():
            names.append(row)
        for idx in range(len(names)):
            if idx != len(names) - 1:
                print(''.join(names[idx]), end=", ")
            else:
                print(''.join(names[idx]), end="\n")
