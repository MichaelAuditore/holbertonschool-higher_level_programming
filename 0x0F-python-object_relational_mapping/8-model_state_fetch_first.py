#!/usr/bin/python3
"""
script that lists all State objects
from the database hbtn_0e_6_usa via SQLAlchemy
"""
if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sqlalchemy as db
    import sys

    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    query = session.query(State).limit(1)
    if query:
        print("{}: {}".format(query.id, query.name))
    else:
        print("Nothing")
