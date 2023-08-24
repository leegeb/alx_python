"""connect to a MySQL database.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Represents a state entity in the database."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128))

    def __init__(self, name):
        """Initialize a State object with a name."""
        self.name = name
