#!/usr/bin/env python3
"""
script that lists all State objects
from the database hbtn_0e_6_usa via SQLAlchemy
"""
if __name__ == "__main__":
    import sqlalchemy as db
    import sys
    if (len(sys.argv) == 5):
        engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
        connection = engine.connect()
        metadata = db.MetaData()
        states = db.Table('states', metadata, autoload=True,
                          autoload_with=engine)
        query = db.select([states.c.id]).where(states.c.name == sys.argv[4])
        Result = connection.execute(query)
        ResultList = Result.fetchall()
        if ResultList == []:
            print("Not found")
        for row in ResultList:
            print("{}".format(row[0]), end="\n")
