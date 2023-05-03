#!/usr/bin/python3
"""
    The file contain the class
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()



class State(Base):
    """
        This class will contain class attribute
    """
    
    __tablename__ = "states"

    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "{} {}".format(self.id, self.name)

#if __name__ == "__main__":
#   engine = create_engine('mysql+mysqldb://root:St@nOk0rie_22@localhost:3306/hbtn_0e_6_usa', pool_pre_ping=True)
#   Base.metadata.create_all(engine) 
if __name__ == "__main__":
    engine = create_engine("sqlite:///hbtn_0e_4_usa", echo=True)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(1, "Arizona")
    session.add(state)
    session.commit()
    s1 = State(2, "California")
    s2 = State(34, "Nevada")
    session.add(s1)
    session.add(s2)
    session.commit()

    results = session.query(State).all()
    print(results)
