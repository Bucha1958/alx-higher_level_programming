#!/usr/bin/python3

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import State, Base
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    create_state = State(name="California")
    create_city = City(name="San Francisco")
    create_state.cities.append(create_city)
    session.add_all([create_state, create_city])
    session.commit()
    session.close()
