#!/usr/bin/python3
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
        The city class 
    """

    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=True)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)


