#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]), post_pre_ping = True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmake(bind=engine)
    session = Session()
    state = State()
    state.id = 6
    state.name = "Louisiana"
    session.add(state)
    session.commit()
    results = session.query(State).order_by(State.id).all()
    for result in results:
        print("{}".format(result.id))
