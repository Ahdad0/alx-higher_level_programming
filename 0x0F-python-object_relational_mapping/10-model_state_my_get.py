#!/usr/bin/python3
"""
prints the State object with the name passed as argument
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    obj = session.query(State).all()

    num = 0
    for ob in obj:
        if sys.argv[4] == ob.name:
            num = 1
            print(f"{ob.id}")

    if num == 0:
        print("Not found")
    session.close()
