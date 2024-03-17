#!/usr/bin/python3
"""first state model"""


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class"""
    __tablename__ = 'states'
    id = Column(Integer,
                primary_key=True,
                unique=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)


engine = create_engine('sqlite:///6-model_state.sql')


if __name__ == '__main__':
    Base.metadata.create_all(engine)
