#!/usr/bin/python3
"""
list all states
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from sqlalchemy.engine.url import URL
import sys


if __name__ == '__main__':
    db = "mysql+pymysql://{}:{}@localhost:3306/{}".
    format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    
    for state in states:
        print('{}: {}'.format(state.id, state.name))
