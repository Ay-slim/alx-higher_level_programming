#!/usr/bin/python3
"""
Module to create the state db table with sqlalchemy ORM
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    A class to declare an object relatio for the states db table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
