#!/usr/bin/python3
"""Adñado el State object louisiana to the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Crear engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Crear sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Crear nuevo estado
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Imprimir el id del nuevo estado
    print(new_state.id)
