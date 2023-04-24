#!/usr/bin/python3
"""
    Script that filter out other state that didn't contain the letter a
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]),
                            pool_pre_ping = True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        result = session.query(State).\
                filter(State.name.ilike("%a%")).order_by(State.id).all()
        for r in result:
            print("{}: {}".format(r.id, r.name))
    except:
        print()
