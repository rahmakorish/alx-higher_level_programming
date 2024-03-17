#!/usr/bin/python3
"""first state model"""


import SQLAlchemy

Base = SQLAlchemy.declarative_base()
class State(Base):
    id:Mapped[int]=mapped_coloumn(primary_key=True, unique=True,\
        nullable = False)
    name:Mapped[str]= mapped_coloumn(nullable=False, max(128))
