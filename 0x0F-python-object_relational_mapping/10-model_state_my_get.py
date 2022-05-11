#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).order_by(State.id)\
        .filter(State.name.like(sys.argv[4])).all()
    if state:
        print("{}".format(state[0].id))
    else:
        print("Not found")
    session.close()
