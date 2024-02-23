#!/usr/bin/python3
"""
prints the first State objects from the database hbtn_0e_6_usa
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

    for ob in obj:
        lenn = len(ob.name)
        num = 0
        while num < lenn:
            if ob.name[num] == 'a' or ob.name[num] == 'A':
                print(f"{ob.id}: {ob.name}")
                break
            num += 1
    session.close()
