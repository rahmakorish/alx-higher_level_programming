#!/usr/bin/python3
"""
List all states
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#not execute unless imported
if __name__ == '__main__':
    engine = create_engine("mysql+pymysql://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).first()
    if states:
        print('{}: {}'.format(states.id, states.name))
    else:
        print('Nothing')
