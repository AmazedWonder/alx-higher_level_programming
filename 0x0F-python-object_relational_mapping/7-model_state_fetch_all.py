#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create an engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # Bind the engine to the Base metadata
    Base.metadata.create_all(engine)
    # Create a session factory
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()
    # Retrieve all State objects and sort them by
    # id in ascending order
    # Display the results
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
    # Close the session
    session.close()
