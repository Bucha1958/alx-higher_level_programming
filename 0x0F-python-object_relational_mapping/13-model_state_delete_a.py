#!/usr/bin/python3

from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).filter(State.name.ilike("%a%")).all()
    for r in results:
        session.delete(r)
    session.commit()
