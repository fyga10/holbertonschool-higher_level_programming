#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy.orm import Session
    from sqlalchemy import (create_engine)

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    session.close()
