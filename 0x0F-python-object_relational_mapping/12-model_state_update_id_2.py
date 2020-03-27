#!/usr/bin/env python3
"""
script that lists all State objects
from the database hbtn_0e_6_usa via SQLAlchemy
"""
if __name__ == "__main__":
    import sqlalchemy as db
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    if (len(sys.argv) == 4):
        engine = db.create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        row = session.query(State).filter(
            State.id == 2).first()
        row.name = "New Mexico"
        session.commit()
        session.close()
