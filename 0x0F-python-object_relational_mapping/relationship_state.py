#!/usr/bin/python3
"""contains the class definition of a State and
an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """inherits from base, links to mysql table states"""
    __tablename__ = 'states'
    id = Column(Integer,
        nullable=False,
        autoincrement=True,
        primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", 
            cascade="all, delete, delete-orphan")
