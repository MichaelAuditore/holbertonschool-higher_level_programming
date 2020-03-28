#!/usr/bin/python3
""" Script to list all cities by state from hbtn_0e_0_usa """
if __name__ == "__main__":
    import MySQLdb as sql
    import sys
    if len(sys.argv) == 4:
        db = sql.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
        c = db.cursor()
        c.execute("""
        SELECT cities.id, cities.name, states.name FROM cities
        RIGHT JOIN states ON cities.state_id = states.id ORDER BY id""")
        for row in c.fetchall():
            print(row)
