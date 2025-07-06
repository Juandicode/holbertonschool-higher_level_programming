#!/usr/bin/python3
"""Definition of the State class and Base instance"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create Base instance
Base = declarative_base()


class State(Base):
    """Class representing the states table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
