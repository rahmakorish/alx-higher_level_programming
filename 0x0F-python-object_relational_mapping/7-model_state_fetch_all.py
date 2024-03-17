#!/usr/bin/python3
"""list all states"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy.engine.url import URL
import sys
if __name__ == '__main__':
    db = {
        'username': sys.argv[1],
        'password': sys.argv[2],
        'drivername': sys.argv[3],
        'host': 'localhost',
        'port': 3306
    }
    engine = create_engine('sqlite:///7-model_state_fetch_all.sql')

    result = engine.execute('SELECT id, name FROM states ORDER BY states.id;')
    for state in result:
        print(state)
