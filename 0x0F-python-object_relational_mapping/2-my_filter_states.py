#!/usr/bin/env python3
""" Script to list all states from hbtn_0e_0_usa with a condition"""
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
        SELECT * FROM states WHERE name=%s ORDER BY id""", (sys.argv[4],))
        for row in c.fetchall():
            print(row)
