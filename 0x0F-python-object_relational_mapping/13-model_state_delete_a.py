#!/usr/bin/python3
"""
script that deletes all State objects with a
name containing the letter a from the database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from sqlalchemy import delete

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).order_by(State.id)\
        .filter(State.name.contains('a')).all()
    for i in state:
        session.delete(i)
    session.commit()
    session.close()
