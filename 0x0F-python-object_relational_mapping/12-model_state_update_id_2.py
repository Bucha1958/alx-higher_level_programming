#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).filter_by(id=2).first()
    results.name = "New Mexico"
    session.commit()
