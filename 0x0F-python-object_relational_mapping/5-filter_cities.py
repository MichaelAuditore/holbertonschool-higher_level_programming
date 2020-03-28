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
    JOIN states ON states.id = cities.state_id
    WHERE states.name=%s ORDER BY cities.id
    """
    c.execute(query, (sys.argv[4],))
    result = [row[0] for row in c.fetchall()]

    print(', '.join(result))
    c.close()
    db.close()
