#!/usr/bin/python3
""" Script to list all cities by state with
 an specific name from hbtn_0e_0_usa """
if __name__ == "__main__":
    import MySQLdb as sql
    import sys

    db = sql.connect(host="localhost",
                     port=3306,
                     user=sys.argv[1],
                     passwd=sys.argv[2],
                     db=sys.argv[3])
    c = db.cursor()
    query = """
    SELECT cities.name FROM cities
    LEFT JOIN states ON states.id = cities.state_id
    WHERE states.name='{}' ORDER BY cities.id
    """.format(sys.argv[4])
    c.execute(query)
    result = [row[0] for row in c.fetchall()]

    print(', '.join(rows))
    c.close()
    db.close()
