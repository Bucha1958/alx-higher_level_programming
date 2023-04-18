#!/usr/bin/python3
"""
    The file contain the class
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()



class State(Base):
    """
        This class will contain class attribute
    """
    
    __tablename__ = "states"

    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

#if __name__ == "__main__":
#   engine = create_engine('mysql+mysqldb://root:St@nOk0rie_22@localhost:3306/hbtn_0e_6_usa', pool_pre_ping=True)
#   Base.metadata.create_all(engine) 
